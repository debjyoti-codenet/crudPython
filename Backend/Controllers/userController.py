from fastapi import HTTPException


from schemas.userSchema import (
    UserRegisterSchema,
    UserLoginSchema,
    UserUpdateSchema
)

from Models.userModel import (
    create_user,
    find_user_by_email,
    get_user_by_id,
    get_all_users,
    delete_user_by_id,
    update_user_by_id
)

from utils.hash import (
    hash_password,
    verify_password
)

from utils.response import (
    api_response_success,
    api_response_error,
    StatusCode
)

from utils.jwt_handler import create_access_token



def register_user(user: UserRegisterSchema):
    try:
        existing_user = find_user_by_email(user.email)

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

        hashed_password = hash_password(user.password)

        new_user = create_user(
            user.name,
            user.email,
            hashed_password
        )
        
        return api_response_success(
            data=new_user,
            success=True,
            response_code=StatusCode.CREATE,
            message="User registered successfully"
        )

    except HTTPException as e:
        raise e

    except Exception as e:
        print("ERROR:", e)
        
        return api_response_error(
            data=None,
            success=False,
            response_code=StatusCode.INTERNAL_SERVER_ERROR,
            err_message="Internal Server Error"
        )



def login_user(user: UserLoginSchema):
    try:
        existing_user = find_user_by_email(user.email)

        if not existing_user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        is_password_correct = verify_password(
            user.password,
            existing_user["password"]
        )

        if not is_password_correct:
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials"
            )

        token = create_access_token({
            "user_id": existing_user["id"],
            "email": existing_user["email"]
        })
        
        return api_response_success(
            data=token,
            success=True,
            response_code=StatusCode.SUCCESS,
            message="Login successful",
            pagination=None
        )


        # return {
        #     "success": True,
        #     "message": "Login successful",
        #     "token": token
        # }
        
    except HTTPException as e:
        raise e

    except Exception as e:
        print("ERROR:", e)

        return api_response_error(
        data=[],
        success=False,
        response_code=StatusCode.INTERNAL_SERVER_ERROR,
        err_message="Something went wrong"
        )


def current_user(user_id):
    try:
        user = get_user_by_id(user_id)

        if not user:
            return api_response_success(
                data=[],
                success=True,
                response_code=StatusCode.BAD_REQUEST,
                message="User not found",
                pagination=None
            )
                     
            
        return api_response_success(
            data=user,
            success=True,
            response_code=StatusCode.SUCCESS,
            message="Successful",
            pagination=None
        )

        # return {
        #     "success": True,
        #     "data": user
        # }
    except HTTPException as e:
        raise e

    except Exception as e:
        print("ERROR:", e)

        return api_response_error(
            data=[],
            success=False,
            response_code=StatusCode.INTERNAL_SERVER_ERROR,
            err_message="Something went wrong"
        )
        
        
    
def all_user_data():

    users = get_all_users()
    
    return api_response_success(
        data=users,
        success=True,
        response_code=StatusCode.SUCCESS,
        message="Successful",
        pagination=None
    )


def delete_user(user_id):

    try:

        deleted_user = delete_user_by_id(user_id)

        if not deleted_user:
            return api_response_error(
                data=[],
                success=False,
                response_code=StatusCode.BAD_REQUEST,
                err_message="User not found"
            )

        return api_response_success(
            data=deleted_user,
            success=True,
            response_code=StatusCode.SUCCESS,
            message="User deleted successfully"
        )

    # except HTTPException as e:
    #     raise e

    except Exception as e:

        print("DELETE USER ERROR:", e)

        return api_response_error(
            data=None,
            success=False,
            response_code=StatusCode.INTERNAL_SERVER_ERROR,
            err_message="Internal Server Error"
        )
        
def update_current_user(
    user_id,
    user: UserUpdateSchema
):

    try:

        existing_user = get_user_by_id(user_id)

        if not existing_user:
            return api_response_error(
                data=[],
                success=False,
                response_code=StatusCode.NOT_FOUND,
                err_message="User not found"
            )

        updated_name = (
            user.name
            if user.name is not None
            else existing_user["name"]
        )

        updated_email = (
            user.email
            if user.email is not None
            else existing_user["email"]
        )

        updated_user = update_user_by_id(
            user_id,
            updated_name,
            updated_email
        )

        return api_response_success(
            data=updated_user,
            success=True,
            response_code=StatusCode.SUCCESS,
            message="User updated successfully"
        )

    except Exception as e:

        print("UPDATE ERROR:", e)

        return api_response_error(
            success=False,
            response_code=500,
            err_message="Internal Server Error"
        )