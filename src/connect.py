import psycopg2
import os

def connect():
    """ Connect to the PostgreSQL database server """
    try:
        conn = psycopg2.connect(
            host=os.environ.get("HOST"),
            database=os.environ.get("DATABASE"),
            user=os.environ.get("USER"),
            password=os.environ.get("PASSWORD")
        )
        print('Connected to the PostgreSQL server.')
        return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    connect()
