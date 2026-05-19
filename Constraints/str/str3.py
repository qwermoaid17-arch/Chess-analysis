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

    def UPEER(cr):

        cr.execute("SELECT text ,UPPER(text) AS upper_text FROM users")

        # Another way

        # cr.execute("SELECT text ,UCASE(text) AS lower_text FROM users")

        result = cr.fetchall()

        for row in result:

            print(f"Text: {row[0]}, Uppercase: {row[1]}")

    def LOWER(cr):

        cr.execute("SELECT text ,LOWER(text) AS lower_text FROM users")

        # Another way

        # cr.execute("SELECT text ,LCASE(text) AS lower_text FROM users")


        result = cr.fetchall()

        for row in result:

            print(f"Text: {row[0]}, Lowercase: {row[1]}")

    UPEER(cr)

    LOWER(cr)

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:
        db.close()