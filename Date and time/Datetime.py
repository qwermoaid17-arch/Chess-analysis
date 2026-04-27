import pymysql as sql
import datetime as dt

try:

    db = sql.connect(
        host = "localhost",
        user = 'root',
        password = "",
    )

    d=dt.datetime.now()

    # d.strftime("%H:%M:%S")

    l=dt.datetime.now()

    date=l.strftime("%Y-%m-%d")
    time=l.strftime("%H:%M:%S")
    timee=l.strftime("%Y-%m-%d %H:%M:%S")
    timing=l.strftime("%Y")
    timo=l.strftime("%Y-%m-%d %H:%M:%S")

    cr=db.cursor()

    cr.execute("CREATE DATABASE IF NOT EXISTS  timing")

    cr.execute("USE timing")

    cr.execute("CREATE TABLE IF NOT EXISTS times (id INT AUTO_INCREMENT PRIMARY KEY , time TIME, timee DATETIME, t DATE, timing YEAR, timo TIMESTAMP ) ")

    cr.execute("INSERT INTO times (time,timee,t,timing,timo) VALUES (%s,%s,%s,%s,%s)",(time,timee,date,timing,timo))

    cr.execute("INSERT INTO times (time, timee, t, timing, timo) VALUES (CURTIME(), NOW(), CURDATE(), YEAR(NOW()), CURRENT_TIMESTAMP)")

    db.commit()

except sql.Error as er:

    print("Error: ",er)