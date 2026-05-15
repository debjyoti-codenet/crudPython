from fastapi import APIRouter, Request
from utils.google_oauth import oauth

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.get("/google")
async def google_login(request: Request):

    redirect_uri = request.url_for("google_callback")
    print(redirect_uri)

    return await oauth.google.authorize_redirect(
        request,
        redirect_uri
    )


@router.get("/google/callback")
async def google_callback(request: Request):

    token = await oauth.google.authorize_access_token(request)

    user = token.get("userinfo")
    print(user)


    return {
        "user": user
    }