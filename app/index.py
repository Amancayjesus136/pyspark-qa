def index():

    # Import views
    from auth.connection_admin import connection_admin
    from auth.connection_user import connection_user  
    from database.database import database_create
    from archive.jdk import jdk_postgres

    # Managing the Postgrest17 Integration Connection
    conn_admin, cur_admin = connection_admin()

    # Integration Database: Create or Delete
    #database_create()

    # Postgrest17 User Integration Connection
    conn, cur = connection_user()

    # Get Spark and configure JDBC
    spark, url, properties = jdk_postgres()

    return spark, url, properties, conn, cur, conn_admin, cur_admin
