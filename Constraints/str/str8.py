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

        cr.execute("INSERT INTO users (text) VALUES (%s)", ("ahmed",))

        cr.execute("INSERT INTO users (text) VALUES (%s)", ("os",))

        cr.execute("INSERT INTO users (text) VALUES (%s)", ("Mah",))

        cr.execute("INSERT INTO users (text) VALUES (%s)", ("OsamaElzero",))

    def SELECT_PAD(cr):

        # cr.execute("SELECT * FROM users")

        # cr.execute("SELECT text as texted, LPAD(text, 5, '') as padded FROM users")

        # cr.execute("SELECT text as texted, LPAD(text, 5, '*') as padded FROM users")

        cr.execute("SELECT text as texted, RPAD(text, 5, '*') as padded FROM users")


        for i in cr:

            print(i[1])

    def UPDATE(cr):

        cr.execute("UPDATE users SET text = RPAD(text, 5, '*') ")
    

    def DELETE(cr):

        cr.execute("DELETE FROM users WHERE id BETWEEN  32 AND 35")

    # INSERT(cr)

    # DELETE(cr)

    UPDATE(cr)

    SELECT_PAD(cr)

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:
        db.close() 