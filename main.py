from typing import Optional

from fastapi import Depends, FastAPI

from fastapi_misskey.client import MisskeyAuthClient
from fastapi.responses import JSONResponse

from fastapi_misskey.exceptions import ClientError

app = FastAPI()

# misskey = MisskeyAuthClient(
#     'https://rn.akarinext.org',
#     'test',
#     'http://localhost:8000/callback',
#     description='FastAPI Misskey Auth'
# )

#VoM1ov7cjJYdfUgqIUY7g1zqrjdi2DDm

misskey = MisskeyAuthClient(
    'https://kr.akirin.xyz',
    'test',
    'http://localhost:8080/callback',
    description='FastAPI Misskey Auth'
)


@app.get('/login')
async def login():
    return {'url': await misskey.get_auth_url()}


@app.get('/callback')
async def callback(session: Optional[str] = None, token: Optional[str] = None):
    token, user = await misskey.get_access_token(session, token)
    response = JSONResponse({'token': token, 'user': user})
    response.set_cookie('token', token)
    return response


@app.get('/profile')
async def profile(user=Depends(misskey.get_user('https://rn.akarinext.org'))):
    return {'user': user}

