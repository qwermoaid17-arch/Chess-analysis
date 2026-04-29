import pymysql as sql

db = sql.connect(
    host = "localhost",
    user = 'root',
    password = "",
)

cr=db.cursor()



cr.execute("CREATE DATABASE IF NOT EXISTS  products")
# cr.execute("CREATE DATABASE IF NOT EXISTS  school")
# cr.execute("DROP DATABASE IF EXISTS school")
cr.execute("USE products")
# cr.execute("DROP DATABASE IF EXISTS moayed")
# cr.execute("DROP TABLE IF EXISTS items")
cr.execute("CREATE TABLE IF NOT EXISTS items (id INT AUTO_INCREMENT PRIMARY KEY , name VARCHAR(255)) ")
cr.execute("INSERT INTO items (name) VALUES (%s)",("منتج6",))
# cr.execute("DELETE FROM items WHERE id BETWEEN %s AND %s", (4,9))
cr.execute("SELECT * FROM items")
f=cr.fetchall()
for i in f:
    print(i)

cr.execute("SHOW DATABASES;")

for i in cr:
    print('-',i[0])

db.commit()