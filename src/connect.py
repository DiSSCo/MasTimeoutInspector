import psycopg2
import os


def connect():
    """ Connect to the PostgreSQL database server """
    try:
        conn = psycopg2.connect(
            host=os.environ["HOST"],
            database=os.environ["DATABASE"],
            user=os.environ["USER"],
            password=os.environ["PASSWORD"]
        )
        print('Connected to the PostgreSQL server.')
        return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    connect()
