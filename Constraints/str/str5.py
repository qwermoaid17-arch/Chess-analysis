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

    def CONCAT(cr):

        # cr.execute("SELECT text , CONCAT(text, ' added by Me') AS cancated FROM users")

        # cr.execute("SELECT text , CONCAT('first ' ,text, ' added by Me') AS cancated FROM users")

        cr.execute("SELECT ID ,text , CONCAT('the country is ', text, ' and its id is ', ID) AS cancated FROM users")



        result = cr.fetchall()

        for row in result:

            print(f"Text: {row[0]}, {row[1]}, {row[2]}")

    def CONCAT_WS(cr):

        # cr.execute("SELECT text , CONCAT(text, ' added by Me') AS cancated FROM users")

        # cr.execute("SELECT text , CONCAT('first ' ,text, ' added by Me') AS cancated FROM users")

        # cr.execute("SELECT ID ,text , CONCAT_WS('-', ID, CONCAT(' ', text)) AS cancated FROM users")

        # cr.execute("SELECT ID ,text , CONCAT_WS('-', ID, REPEAT(text, 2)) AS cancated FROM users")

        cr.execute("SELECT ID ,text , REVERSE(CONCAT(ID, text, 'osama')) AS cancated FROM users")





        result = cr.fetchall()

        for row in result:

            print(f"Text: {row[0]}, {row[1]}, {row[2]}")

    # CONCAT(cr)

    CONCAT_WS(cr)


    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:
        db.close()