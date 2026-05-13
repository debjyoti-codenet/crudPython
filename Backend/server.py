from fastapi import FastAPI
from Config.db import get_connection
from Routes.userRoutes import router as userRouter
app = FastAPI()
app.include_router(userRouter)

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