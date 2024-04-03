import psycopg2
from connect import connect


def update_timeout():
    updated_row_count = 0
    sql = """
    update public.mas_job_record
    set error = 'TIMEOUT', job_state = 'FAILED'
    where time_to_live < (select CURRENT_TIMESTAMP) and job_state = 'SCHEDULED';
    """

    try:
        with connect() as conn:
            with conn.cursor() as cur:
                updated_row_count = cur.execute(sql)
                updated_row_count = cur.rowcount
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        print(updated_row_count, "jobs marked as timed out.")


if __name__ == '__main__':
    update_timeout()
