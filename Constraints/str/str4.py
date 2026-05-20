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

    def INSERT(cr):

        cr.execute("INSERT INTO users (text) VALUES (%s)", ("http://www.elzero.info",))

        cr.execute("INSERT INTO users (text) VALUES (%s)", ("http://www.facebook.com",))

    def REPEAT(cr):

        cr.execute("SELECT text , REPEAT(text, 3) AS repeated FROM users")

        result = cr.fetchall()

        for row in result:

            print(f"Text: {row[0]}, Repeated: {row[1]}")

    def REPLACE(cr):

        # cr.execute("SELECT text , REPLACE (text, 'a', '@') AS replaced FROM users")

        cr.execute("SELECT text , REPLACE (text, 'http', 'https') AS replaced FROM users")


        result = cr.fetchall()

        for row in result:

            print(f"Text: {row[0]}, Replaced: {row[1]}")

            print("-------------------------------------------------------------")

    def UPDATE(cr):

        # cr.execute("UPDATE users SET text = REPLACE (text, 'http', 'https')")

        # cr.execute("UPDATE users SET text = REPLACE (text, 'https://.www', '')")

        cr.execute("UPDATE users SET text = REVERSE(text)")

    def reverse(cr):

        cr.execute("SELECT text , REVERSE(text) AS reversed FROM users")

        result = cr.fetchall()

        for row in result:

            print(f"Text: {row[0]}, Reversed: {row[1]}")


    def show(cr):

        cr.execute("SELECT text FROM users")

        result = cr.fetchall()

        for row in result:

            print(f"Text: {row[0]}")

    def delete(cr):

        cr.execute("DELETE FROM users WHERE text LIKE '%.%'")

    # REPEAT(cr)

    # print("*" * 50)

    # REPLACE(cr)

    # UPDATE(cr)

    # reverse(cr)

    delete(cr)

    show(cr)  

    # INSERT(cr)

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:
        db.close()