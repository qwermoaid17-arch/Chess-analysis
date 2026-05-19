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

    def INSERT_users(cr):

        cr.execute("INSERT INTO users (text) VALUES (%s)", ("MOAYS",))

    def LEN(cr):

        cr.execute("SELECT text ,LENGTH(text) AS count FROM users")

        result = cr.fetchall()

        for row in result:

            print(f"Text: {row[0]}, Length: {row[1]}")

    def CHAR_LEN(cr):

        # cr.execute("SELECT text ,CHAR_LENGTH(text) AS count FROM users")

        # cr.execute("SELECT text ,CHAR_LENGTH(text) AS count FROM users ORDER BY CHAR_LENGTH(text) ASC")

        cr.execute("SELECT text ,CHAR_LENGTH(text) AS count FROM users ORDER BY CHAR_LENGTH(text) DESC")

        result = cr.fetchall()

        for row in result:

            print(f"Text: {row[0]}, Length: {row[1]}")

    CHAR_LEN(cr)

    # INSERT_users(cr)

    # LEN(cr)

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:
        db.close()