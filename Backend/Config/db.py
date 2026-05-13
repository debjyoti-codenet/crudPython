import os

import psycopg2 # Python ko PostgreSQL database se connect karne ka bridge 
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    conn = psycopg2.connect(
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        cursor_factory=RealDictCursor
    )

    return conn

#RealDictCursor -> db call response
# [
#   {'id': 1, 'name': 'John'},
#   {'id': 2, 'name': 'Alex'}
# ]

# else response normal cursor -> 
# [
#     [(1, 'John'), (2, 'Alex')]
# ]
