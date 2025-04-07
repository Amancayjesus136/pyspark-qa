from pyspark.sql import SparkSession
import socket
import os

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
os.environ["SPARK_LOCAL_IP"] = local_ip

def jdk_postgres():
    spark = SparkSession.builder \
        .appName("ReadPostgres") \
        .config("spark.jars", "/home/linux-adrian/Documents/pyspark/drivers/postgresql-42.7.5.jar") \
        .config("spark.ui.port", "4050")  \
        .config("spark.hadoop.native.lib", "false")  \
        .config("spark.executor.memory", "4g")  \
        .config("spark.driver.memory", "2g")  \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    url = "jdbc:postgresql://localhost:5432/db_casa"
    properties = {
        "user": "postgres",
        "password": "lima2025@",
        "driver": "org.postgresql.Driver"
    }

    return spark, url, properties
