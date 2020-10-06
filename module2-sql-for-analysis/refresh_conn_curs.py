# Define a function to refresh connection and cursor
def refresh_connection_and_cursor(conn, curs):
  curs.close()
  conn.close()
  pg_conn = psycopg2.connect(dbname=dbname, user=user,
                             password=password, host=host)
  pg_curs = pg_conn.cursor()
  return pg_conn, pg_curs