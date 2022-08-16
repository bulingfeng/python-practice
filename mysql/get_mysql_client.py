import pymysql as mysql


def get_mysql_client():
    db = mysql.connect(host='127.0.0.1',
                       user='root',
                       password='1234567',
                       database='e_commerce')
    return db
