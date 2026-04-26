import pymysql as sql
import datetime as dt

try:
    db = sql.connect(
        host = "localhost",
        user = 'root',
        password = "",
    )


    age=20

    subscription_months=2

    a=dt.datetime(2024, 6, 1)

    join_year=a.strftime("%Y")

    b=dt.datetime(2006, 2, 1)

    join_month=b.strftime("%Y-%m-%d")

    c=dt.datetime(2026, 4, 1, 8, 30, 45)

    last_visit_time=c.strftime("%H:%M:%S")

    d=dt.datetime(2024, 6, 1, 12, 30, 45)

    registration_stamp=d.strftime("%Y-%m-%d %H:%M:%S")



    cr=db.cursor()

    cr.execute("CREATE DATABASE IF NOT EXISTS  gym_system")

    cr.execute("USE gym_system")

    cr.execute("CREATE TABLE IF NOT EXISTS members (id INT AUTO_INCREMENT PRIMARY KEY , age TINYINT, months TINYINT, join_year Year, join_month DATE, last_visit_time TIME, registration_stamp DATETIME) ")


    cr.execute("INSERT INTO members (age, months, join_year, join_month, last_visit_time, registration_stamp) VALUES (%s,%s,%s,%s,%s,%s)",(age, subscription_months, join_year, join_month, last_visit_time, registration_stamp))

    db.commit()

    db.close()

except sql.Error as er:
    print("Error : ", er)

print("Data inserted successfully")