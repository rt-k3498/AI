from psycopg_pool import ConnectionPool
import os

db_url = os.getenv("DATABASE_URL")

class PGPooler: 
    def __init__(self):
        self.pool = ConnectionPool(db_url, min_size=1, max_size=5)

    def query(self, query: str, params: tuple = None):
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                if cur.description:
                    return cur.fetchall()
                else:
                    return None

