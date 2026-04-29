import pymysql as sql

try:

    db = sql.connect(
        host = "localhost",
        user ="root",
        password = "",
        charset='utf8mb4'
    )
    cr = db.cursor()

    cr.execute("CREATE DATABASE IF NOT EXISTS moayed")

    cr.execute("SHOW DATABASES like 'moayed'")


    for i in cr:
        print('-',i[0])

    cr.execute("USE moayed")   

    cr.execute("DROP DATABASE IF EXISTS moayed")


    
except sql.Error as er:
    print("Error ", er)