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

        # cr.execute("INSERT INTO num (number) VALUES (%s)", (123456.6565656,))

        # cr.execute("INSERT INTO num (number) VALUES (TRUNCATE(%s, 2))", (123456.6565656,))

        cr.execute("INSERT INTO num (number) VALUES (%s)", (2,))

        cr.execute("INSERT INTO num (number) VALUES (%s)", (3,))

        cr.execute("INSERT INTO num (number) VALUES (%s)", (4,))


    def TRANCAT(cr):

        # cr.execute("SELECT number ,ROUND(number, 2), TRUNCATE(number, 2) FROM num")

        cr.execute("SELECT number ,ROUND(number, 3), TRUNCATE(number, 3) FROM num")


        result = cr.fetchall()

        for row in result:

            print(f"Number: {row[0]}, Round: {row[1]}, Truncate: {row[2]}")

    def SELECT_pow(cr):

        cr.execute("SELECT number ,POWER(number, 2) FROM num")

        # cr.execute("SELECT number ,POWER(number, id) FROM num")

        result = cr.fetchall()

        for row in result:

            print(f"Number: {row[0]}, Power: {row[1]}")

    def SELECT_MOD(cr):

        # cr.execute("SELECT number ,MOD(7, 2) FROM num")

        # cr.execute("SELECT number ,MOD(21, 5) FROM num")

        # cr.execute("SELECT number ,MOD(22, 5) FROM num")

        # cr.execute("SELECT number ,MOD(23, 5) FROM num")

        cr.execute("SELECT number ,MOD(25, 5) FROM num")

        result = cr.fetchall()

        for row in result:

            print(f"Number: {row[0]}, Mod: {row[1]}")

    def SELECT_ABS(cr):

        cr.execute("SELECT number ,ABS(-9) FROM num")

        result = cr.fetchall()

        for row in result:

            print(f"Number: {row[0]}, Abs: {row[1]}")
    
    def SELECT_SQRT(cr):

        cr.execute("SELECT number ,SQRT(number) FROM num")

        result = cr.fetchall()

        for row in result:

            print(f"Number: {row[0]}, Sqrt: {row[1]}")

    def DELETE(cr):

        cr.execute("DELETE FROM num WHERE id BETWEEN  1 AND 20")



    #Calling functions :

    # INSERT(cr)

    # TRANCAT(cr)

    # DELETE(cr)

    # SELECT_pow(cr)

    # SELECT_MOD(cr)

    # SELECT_ABS(cr)

    SELECT_SQRT(cr)

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:
        db.close()