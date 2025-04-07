import psycopg2

def connection_user():
    conn = psycopg2.connect(
        dbname="db_casa",
        user="postgres",
        password="lima2025@",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    return conn, cur  

if __name__ == "__main__":
    conn, cur = connection_user()

    cur.close()
    conn.close()
