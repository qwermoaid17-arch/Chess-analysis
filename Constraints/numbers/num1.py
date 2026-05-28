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

    # cr.execute("DROP TABLE IF EXISTS num")

    cr.execute("CREATE TABLE IF NOT EXISTS num (id INT AUTO_INCREMENT PRIMARY KEY, number double)")


    def INSERT(cr):

        cr.execute("INSERT INTO num (number) VALUES (%s)", (1.2,))

        cr.execute("INSERT INTO num (number) VALUES (%s)", (1.45,))

        cr.execute("INSERT INTO num (number) VALUES (%s)", (1.55,))

        cr.execute("INSERT INTO num (number) VALUES (%s)", (1.456789,))

        cr.execute("INSERT INTO num (number) VALUES (%s)", (1.99,))

        cr.execute("INSERT INTO num (number) VALUES (%s)", (1.49999,))

        cr.execute("INSERT INTO num (number) VALUES (%s)", (1.5,))

    def ceil(cr):
        
        cr.execute("SELECT number ,CEIL(number) FROM num")

        result = cr.fetchall()

        for row in result:

            print(f"Number: {row[0]}, Ceil: {row[1]}")

    def FLOOR(cr):

        cr.execute("SELECT number ,FLOOR(number) FROM num")

        result = cr.fetchall()

        for row in result:

            print(f"Number: {row[0]}, Floor: {row[1]}")

    def ROUND(cr):

        # cr.execute("SELECT number ,ROUND(number) FROM num")

        cr.execute("SELECT number ,ROUND(number, 2) FROM num")

        result = cr.fetchall()

        for row in result:

            print(f"Number: {row[0]}, Round: {row[1]}")

    def UPDATE(cr):

        # cr.execute("UPDATE num SET number = 1.491111 WHERE id = 6")

        cr.execute("UPDATE num SET number = %s WHERE id = %s", (1.599, 7))


    # Calling the function:

    # INSERT(cr)

    # ceil(cr)

    # FLOOR(cr)

    UPDATE(cr)

    ROUND(cr)

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:
        db.close()