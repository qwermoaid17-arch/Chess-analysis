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

        # cr.execute("INSERT INTO users (text) VALUES (%s)", ("123Elzero1212121212",))

        # cr.execute("INSERT INTO users (text) VALUES (%s)", ("123Elzero1313131313",))

        # cr.execute("INSERT INTO users (text) VALUES (%s)", ("123Elzero1414141414",))

        cr.execute("INSERT INTO users (text) VALUES (%s)", ("ASDASD#",))

        cr.execute("INSERT INTO users (text) VALUES (%s)", ("ASDASD#",))

        cr.execute("INSERT INTO users (text) VALUES (%s)", ("ASDASD#",))


    def UPDATE(cr):

        # cr.execute("UPDATE users SET text = INSERT(text, 4, 6, 'serial')")

        # cr.execute("UPDATE users SET text = INSERT(text, 4, 6, 'mantel') WHERE text = '123serial1212121212'")

        # cr.execute("UPDATE users SET text = INSERT(text, 6, 4, '#')")

        # cr.execute("UPDATE users SET text = %s WHERE id = %s", ("ASDASD#", 20))

        cr.execute("UPDATE users SET text = INSERT(text, 7, 1, id)")



    def SELECT_INSERT(cr):

        # cr.execute("SELECT text FROM users")

        cr.execute("SELECT text, INSERT(text, 3, 2, 'moayed') as inserted FROM users")

        result = cr.fetchall()

        for row in result:

            print(f"Text: {row[0]}, Inserted: {row[1]}")

    def show (cr):

        cr.execute("SELECT text FROM users")

        result = cr.fetchall()

        for row in result:

            print(f"Text: {row[0]}")

    def delete(cr):

        # cr.execute("DELETE FROM users WHERE id BETWEEN  1 AND 11")

        cr.execute("DELETE FROM users WHERE id BETWEEN  21 AND 22")




    # INSERT(cr)

    # SELECT_INSERT(cr)

    # delete(cr)

    UPDATE(cr)

    show(cr)

    cr.execute


    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:
        db.close()