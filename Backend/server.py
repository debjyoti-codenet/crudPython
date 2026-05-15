from fastapi import FastAPI
from Config.db import get_connection
from Routes.userRoutes import router as userRouter
from Routes.authRouter import router as authRouter
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
app.include_router(userRouter) #from Routes.userRoutes import router as userRouter
app.include_router(authRouter)

app.add_middleware(
    SessionMiddleware,
    secret_key="rjJ+2MwBDdzT5H0rv5y8bik3EB1Fdq6owWrFPl5J07c="
)

@app.get("/")
def home():

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT NOW()")

        data = cursor.fetchone()

        cursor.close()
        conn.close()

        return {
            "message": "Database Connected! http://127.0.0.1:8000",
            "time": data
        }

    except Exception as e:
        return {
            "error": str(e)
        }