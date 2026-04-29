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

    # cr.execute("DROP TABLE IF EXISTS yy")

    # cr.execute("CREATE TABLE IF NOT EXISTS y1 "
    # "(id INT AUTO_INCREMENT PRIMARY KEY, " \
    # " name VARCHAR(255), " \
    # "email VARCHAR(255))")

    # for i in cr:
    #     print(i)

    # cr.execute("RENAME TABLE y2 TO y3, y TO y2")
    cr.execute("ALTER TABLE y1 ENGINE = MyISAM")

    # cr.execute("SHOW DATABASES")

    # for i in cr:
    #     print(i)

    cr.execute("SHOW TABLE STATUS FROM moayed")

    for i in cr:
        print(i)

    # cr.execute("SHOW COLUMNS FROM students")

    # for i in cr:
    #     print(i)

    db.commit()
    db.close()

except sql.Error as er:
    print("Error ", er)