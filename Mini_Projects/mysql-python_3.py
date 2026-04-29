import pymysql as sql

try:

    db = sql.connect(
        host = "localhost",
        user="root",
        passwd="",
        charset="utf8mb4"
    )

    cr = db.cursor()

    cr.execute("CREATE DATABASE IF NOT EXISTS hi")
    cr.execute("USE hi")
    
    cr.execute("SHOW DATABASES like 'hi'")

    for i in cr:
        print('-', i[0])

    cr.execute("DROP DATABASE IF EXISTS hi")

except sql.Error as er:
    print("Error ", er)