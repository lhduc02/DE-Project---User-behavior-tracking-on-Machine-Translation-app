import pandas as pd
import pymysql

def connect_to_starrocks():
    HOST = "localhost"  # Ví dụ: "127.0.0.1"
    PORT = 9030  # Mặc định của StarRocks
    USER = "root"
    PASSWORD = ""
    DATABASE = "event_logs"

    # Kết nối tới StarRocks
    conn = pymysql.connect(
        host=HOST, port=PORT, user=USER, password=PASSWORD, database=DATABASE
    )
    return conn
