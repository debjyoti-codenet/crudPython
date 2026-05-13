from fastapi.responses import JSONResponse


class StatusCode:
    SUCCESS = 200
    CREATE = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409
    INTERNAL_SERVER_ERROR = 500


def api_response_success(
    data=None,
    success=True,
    response_code=200,
    message="Success",
    pagination=None
):

    return JSONResponse(
        status_code=response_code,
        content={
            "data": data,
            "success": success,
            "responseCode": response_code,
            "message": message,
            "pagination": pagination
        }
    )


def api_response_error(
    data=None,
    success=False,
    response_code=500,
    err_message="Something went wrong"
):

    return JSONResponse(
        status_code=response_code,
        content={
            "data": data,
            "success": success,
            "responseCode": response_code,
            "errMessage": err_message
        }
    )