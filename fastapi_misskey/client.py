import hashlib
import json
import uuid
from typing import List, Optional
from urllib.parse import urlencode

import aiohttp
from aiocache import cached
from fastapi import Request

from fastapi_misskey.exceptions import NotCompletedAuthException, SomethingWasWrong
from fastapi_misskey.models import User
from fastapi_misskey.utils import remove_empty_dict


class MisskeyAuthClient:
    """
    Client for Misskey Auth.
    """

    def __init__(self, host: str,
                 name: str,
                 callback: str,
                 description: str,
                 permissions: Optional[List[str]]=None,
                 *,
                 icon: Optional[str] = None
                 ):
        if permissions is None:
            permissions = ['read:account']
        self.host: str = host
        self.name: str = name
        self.callback: str = callback
        self.permissions: List[str] = permissions
        self.description: str = description
        self.icon: Optional[str] = icon
        self.secret = None
        self._client_session: aiohttp.ClientSession = aiohttp.ClientSession()

    @cached(ttl=550)
    async def check_support_miauth(self):
        """
        miauth をサポートしているインスタンスか否かを返します(v10, v11 と v12の区別)
        """
        
        async with self._client_session.post(f'{self.host}/api/meta') as res:
            data = await res.json()
            return bool(data.get('miauth'))

    async def get_auth_url(self):
        """
        認証に使用するurlを生成して返します
        """
        
        field = await remove_empty_dict({'name': self.name, 'description': self.description})
        if await self.check_support_miauth():
            field['callback'] = self.callback
            field['permissions'] = self.permissions
            query = urlencode(field)
            return f'{self.host}/miauth/{uuid.uuid4()}?{query}'
        else:
            field['callbackUrl'] = self.callback
            field['permission'] = self.permissions
            async with self._client_session.post(f'{self.host}/api/app/create', data=json.dumps(field, ensure_ascii=False)) \
                    as res:
                data = await res.json()
                self.secret = data['secret']
            field = json.dumps({'appSecret': self.secret}, ensure_ascii=False)
            async with self._client_session.post(f'{self.host}/api/auth/session/generate', data=field) as res:
                data = await res.json()
                return data['url']

    @cached(ttl=550)
    async def get_access_token(self, session_code: Optional[str] = None, token: Optional[str] = None):
        """
        ユーザーのアクセストークンを取得します
        """
        
        if self.secret is None:
            raise SomethingWasWrong()
        if await self.check_support_miauth():
            async with self._client_session.post(f'{self.host}/api/miauth/{session_code}/check') as res:
                data = await res.json()
                if data.get('ok'):
                    return data.get('token'), data.get('user')
                else:
                    raise NotCompletedAuthException()
        else:
            field = {'appSecret': self.secret, 'token': token}
            async with self._client_session.post(f'{self.host}/api/auth/session/userkey', data=json.dumps(field)) as res:
                data = await res.json()
                access_token = data['accessToken']
                return hashlib.sha256(f'{access_token + self.secret}'.encode('utf-8')).hexdigest(), data.pop('accessToken')

    @cached(ttl=550)
    async def get_user(self, request: Request) -> User:
        """
        アクセストークンのユーザーを取得します
        """
        
        token = request.headers.get('Authorization')
        field = {'i': token}
        async with self._client_session.post(f'{self.host}/api/i', json=field) as res:
            data = await res.json()
            return User(**data)
