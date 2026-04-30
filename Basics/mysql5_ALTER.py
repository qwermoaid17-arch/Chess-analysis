import pymysql as sql

try:

    db = sql.connect(
        host = "localhost",
        user="root",
        passwd="",
        charset='utf8mb4'
    )

    cr = db.cursor()

    cr.execute("CREATE DATABASE IF NOT EXISTS moayed ")
    cr.execute("USE moayed")

    cr.execute("CREATE TABLE IF NOT EXISTS students "
    "(id INT AUTO_INCREMENT PRIMARY KEY, " \
    " name VARCHAR(255), " \
    "email VARCHAR(255))")

    cr.execute("ALTER TABLE students ADD COLUMN if NOT EXISTS password VARCHAR(255)")

    cr.execute("ALTER TABLE students ADD COLUMN if NOT EXISTS username VARCHAR(255) AFTER name")

    cr.execute("ALTER TABLE students ADD COLUMN if NOT EXISTS test VARCHAR(255) FIRST")

    cr.execute("ALTER TABLE students ADD COLUMN if NOT EXISTS end VARCHAR(255)")

    cr.execute("ALTER TABLE students ADD COLUMN if NOT EXISTS last VARCHAR(255)")

    cr.execute("ALTER TABLE students DROP COLUMN last")

    cr.execute("ALTER TABLE students DROP COLUMN end")

    # cr.execute("ALTER TABLE students CHANGE COLUMN IF EXISTS username username VARCHAR(255) AFTER email")

# test error
    # cr.execute("ALTER TABLE students CHANGE COLUMN IF EXISTS username username  AFTER test")

    cr.execute("ALTER TABLE students CHANGE COLUMN IF EXISTS username username VARCHAR(255) AFTER password")

    # cr.execute("ALTER TABLE students CHANGE COLUMN IF EXISTS test test CHAR(50)")

    # cr.execute("ALTER TABLE students MODIFY COLUMN IF EXISTS test VARCHAR(255)")

    cr.execute("ALTER TABLE students CHANGE COLUMN IF EXISTS test maoyed char(50)")



    # cr.execute("SHOW DATABASES")

    # for i in cr:

    #     print(i[0])

except sql.Error as er:
    print("Error ", er)