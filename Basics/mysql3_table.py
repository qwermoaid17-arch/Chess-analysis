import pymysql as sql

try:

    db = sql.connect(
        host = "localhost",
        user = "root",
        password = "",
        charset='utf8mb4'
    )

    cr = db.cursor()

    cr.execute("CREATE DATABASE IF NOT EXISTS moayed")

    # cr.execute("SHOW DATABASES")

    # for i in cr:

    #     print(i[0])

    cr.execute("USE moayed")

    cr.execute("DROP TABLE IF EXISTS yy")

    # cr.execute("CREATE TABLE IF NOT EXISTS yy "
    # "(id INT AUTO_INCREMENT PRIMARY KEY, " \
    # " name VARCHAR(255), " \
    # "email VARCHAR(255))")

    # cr.execute("SHOW COLUMNS FROM students")

    # for i in cr:
    #     print(i)

    # cr.execute("SHOW TABLE STATUS FROM moayed")

    # cr.execute("SHOW CREATE TABLE yy")



    for i in cr:
        print(i)

    db.commit()
    db.close()

except sql.Error as er:
    print("Error ", er)