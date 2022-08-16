# in查询
import get_mysql_client as client

db = client.get_mysql_client()

cursor = db.cursor()
name = """'blf'"""
ids = (11, 12,)
sql = 'select * from t_ecommerce_user where id in %s and username=%s' % (ids, name)
print(sql)
cursor.execute(sql)

data = cursor.fetchall()

for item in data:
    print(item)
