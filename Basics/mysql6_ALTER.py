import pymysql as sql

try:

    db = sql.connect(
        host = "localhost",
        user="root",
        passwd="",
        charset='utf8mb4'
    )

    cr = db.cursor()

    cr.execute("CREATE DATABASE IF NOT EXISTS moayed")
    cr.execute("USE moayed")

    cr.execute("CREATE TABLE IF NOT EXISTS students "
    "(id INT AUTO_INCREMENT PRIMARY KEY, " \
    " name VARCHAR(255), " \
    "email VARCHAR(255))")

    o = cr.execute("SHOW TABLES LIKE 'y3'")

    if o == 1:

        cr.execute("ALTER TABLE y3 RENAME TO yy")
    
    else:

        pass

    # cr.execute("ALTER TABLE students MODIFY COLUMN username char(50), CHANGE  COLUMN id user_id INT(11)")

    # cr.execute("ALTER TABLE students MODIFY COLUMN username VARCHAR(255), CHANGE  COLUMN user_id id TINYINT(1)")

    cr.execute("ALTER TABLE students  CONVERT TO CHARACTER SET utf8mb4")

    cr.execute("SHOW DATABASES")

    for i in cr:

        print(i[0])

except sql.Error as er:

    print("Error ", er)