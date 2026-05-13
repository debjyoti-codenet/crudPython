from fastapi import APIRouter, Depends

from Controllers.userController import (
    register_user,
    login_user,
    current_user,
    all_user_data,
    delete_user,
    update_current_user
)

from schemas.userSchema import (
    UserRegisterSchema,
    UserLoginSchema,
    UserUpdateSchema
)

from Middleware.authMiddleware import auth_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/register")
def register(user: UserRegisterSchema):
    return register_user(user)


@router.post("/login")
def login(user: UserLoginSchema):
    return login_user(user)


@router.get("/me")
def get_me(user=Depends(auth_user)):
    return current_user(user["user_id"])

@router.get("/all")
def all_user():
    return all_user_data()

@router.delete("/delete/{user_id}")
def remove_user(user_id:int):
    return delete_user(user_id)

@router.put("/update/{user_id}")
def update_user_by_id(
    user_id: int,
    update_data: UserUpdateSchema
):
    return update_current_user(
        user_id,
        update_data
    )