import psycopg2

def connection_admin():
    """Creates and returns a connection and cursor to the PostgreSQL database."""
    try:
        conn_admin = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="lima2025@", 
            host="localhost",
            port="5432"
        )
        conn_admin.autocommit = True
        cur_admin = conn_admin.cursor()
        print("✅ Connection and cursor created successfully.")
        return conn_admin, cur_admin
    
    except Exception as e:
        print(f"❌ Error connecting to PostgreSQL: {e}")
        raise  
    
if __name__ == "__main__":
    conn_admin, cur_admin = connection_admin()
    
    cur_admin.close()
    conn_admin.close()
