from auth.connection_admin import connection_admin  

def database_create():
    conn_admin, cur_admin = connection_admin()  

    cur_admin.execute("DROP DATABASE IF EXISTS db_casa;")
    cur_admin.execute("CREATE DATABASE db_casa OWNER postgres;")