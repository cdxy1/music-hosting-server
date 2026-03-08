import psycopg2

from src.infrastructure.config.postgres import PostgresConfig


def run_sql(query, args):
    uri = PostgresConfig().sync_database_uri
    with psycopg2.connect(uri) as conn:
        with conn.cursor() as cur:
            
            if args:
                cur.execute(query, args)
            else:
                cur.execute(query)
            
            if cur.description:
                return cur.fetchall()
