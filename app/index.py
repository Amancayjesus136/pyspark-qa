def index():

    from auth.connection_admin import connection_admin
    from auth.connection_user import connection_user  
    from database.database import database_create
    from archive.jdk import jdk_postgres

    conn_admin, cur_admin = connection_admin()

    #database_create()

    conn, cur = connection_user()

    spark, url, properties = jdk_postgres()

    return spark, url, properties, conn, cur, conn_admin, cur_admin
