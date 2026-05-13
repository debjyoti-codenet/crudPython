from fastapi import Header, HTTPException

from utils.jwt_handler import verify_access_token


def auth_user(authorization: str = Header(None)):

    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Authorization token missing"
        )

    try:

        token = authorization.split(" ")[1]

        decoded = verify_access_token(token)

        return decoded

    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )