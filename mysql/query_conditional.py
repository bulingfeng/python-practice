# 条件查询
import pymysql
import get_mysql_client as client

db = client.get_mysql_client()
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# (11, 'blf', '1234567'
sql='select * from t_ecommerce_user where username =%s' % """'blf'"""
print(sql)
cursor.execute(sql)

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()
# 打印
for item in data:
    print(item)

# 关闭数据库连接
db.close()