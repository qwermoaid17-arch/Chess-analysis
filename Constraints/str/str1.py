import pymysql as sql

try:

    db = sql.connect(
        host = "localhost",
        user = "root",
        password = "",
        charset='utf8mb4'
    )

    cr = db.cursor()

    cr.execute("USE tests")

    cr.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, text VARCHAR(100))")

    def INSERT_users(cr):

        cr.execute("INSERT INTO users (text) VALUES (%s)", ("libya",))

        cr.execute("INSERT INTO users (text) VALUES (%s)", ("sudia arabia",))

        cr.execute("INSERT INTO users (text) VALUES (%s)", ("egypt",))

    def show_users(cr):

        #  cr.execute("SELECT LEFT(text, 2) FROM users")
        

        # cr.execute("SELECT RIGHT(text, 3) FROM users")

        # cr.execute("SELECT MID(text, 2, 3) FROM users")

        cr.execute("SELECT MID(text, 5, 4) FROM users")


        result = cr.fetchall()

        for row in result:

            print(row[0])

    # INSERT_users(cr)

    show_users(cr)

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:
        db.close()