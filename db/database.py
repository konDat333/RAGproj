import psycopg
import os
from dotenv import load_dotenv

load_dotenv()



def get_connection():
    conn = psycopg.connect(
        f"postgresql://{os.environ.get('DATABASE_USER')}:{os.environ.get('DATABASE_PASSWORD')}@localhost:{os.environ.get('DATABASE_PORT')}/{os.environ.get('DATABASE_NAME')}",
        autocommit=False,
    )
    return conn
