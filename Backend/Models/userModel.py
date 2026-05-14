from Config.db import get_connection
from psycopg2.extras import RealDictCursor

def create_user(name, email, password):

    conn = get_connection()# create connection
    cursor = conn.cursor() #execution object communicate with sql

    query = """
        INSERT INTO users(name, email, password)
        VALUES(%s, %s, %s)
        RETURNING id, name, email
    """
    
    # triple quets (""") used for multiline string

    cursor.execute(query, (name, email, password))

    user = cursor.fetchone() # fetch ONLY first row

    conn.commit()

    cursor.close()
    conn.close()

    return user


def find_user_by_email(email):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT * FROM users
        WHERE email = %s
    """

    cursor.execute(query, (email,))

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user


def get_user_by_id(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT id, name, email
        FROM users
        WHERE id = %s
    """

    cursor.execute(query, (user_id,))

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user


def get_all_users():

    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    query = "SELECT id, name, email FROM users"

    cursor.execute(query)

    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return users

def delete_user_by_id(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        DELETE FROM users
        WHERE id = %s
        RETURNING id, name, email
    """

    cursor.execute(query, (user_id,))

    deleted_user = cursor.fetchone()

    conn.commit()

    cursor.close()
    conn.close()

    return deleted_user

def update_user_by_id(
    user_id,
    name,
    email
):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE users
        SET name = %s,
            email = %s
        WHERE id = %s
        RETURNING id, name, email
    """

    cursor.execute(
        query,
        (name, email, user_id)
    )

    updated_user = cursor.fetchone()

    conn.commit()

    cursor.close()
    conn.close()

    return updated_user