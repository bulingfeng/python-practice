import pymysql as mysql

db = mysql.connect(host='127.0.0.1',
                   user='root',
                   password='1234567',
                   database='e_commerce')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("select * from t_ecommerce_user ")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()
# 打印
for item in data:
    print(item)

# 关闭数据库连接
db.close()
