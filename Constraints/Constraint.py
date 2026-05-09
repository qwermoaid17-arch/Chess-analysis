import pymysql as sql

try:

    db = sql.connect(
        host = "localhost",
        user = "root",
        password = "",
        charset='utf8mb4'
    )

    cr = db.cursor()

    cr.execute("USE moayed")

    # cr.execute("INSERT INTO students (maoyed, id, name, email, password, username) VALUES (%s, %s, %s, %s, %s, %s)", (None , None, None, None, None, None))

    cr.execute("ALTER TABLE students CHANGE COLUMN username username VARCHAR(255) NOT NULL")

    cr.execute("ALTER TABLE students ADD COLUMN ahmed VARCHAR(255) NOT NULL")

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:
    
    if db:
        db.close()