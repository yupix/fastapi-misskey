from typing import Optional

from fastapi import Depends, FastAPI

from fastapi_misskey.client import MisskeyAuthClient

app = FastAPI()

# misskey = MisskeyAuthClient(
#     'https://rn.akarinext.org',
#     'test',
#     'http://localhost:8000/callback',
#     description='FastAPI Misskey Auth'
# )

misskey = MisskeyAuthClient(
    'https://kr.akirin.xyz',
    'test',
    'http://localhost:8000/callback',
    description='FastAPI Misskey Auth'
)


@app.get('/login')
async def login():
    return {'url': await misskey.get_auth_url()}


@app.get('/callback')
async def callback(session: Optional[str] = None, token: Optional[str] = None):
    token, user = await misskey.get_access_token(session, token)
    return {'token': token, 'user': user}


@app.get('/profile')
async def profile(user=Depends(misskey.get_user)):
    if user.get('error'):
        return user
    else:
        return {'user': user}

