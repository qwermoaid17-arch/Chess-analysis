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



    cr.execute("CREATE TABLE IF NOT EXISTS chess(my_rating INT(4), oppoenent_rating INT, game_duration DOUBLE)")


    def INSERT(cr):

        cr.execute("INSERT INTO chess(my_rating, oppoenent_rating, game_duration) VALUES (%s, %s, %s)", (718, 766, 9.15))

    def DELTE(cr):

        cr.execute("DELETE FROM chess WHERE oppoenent_rating = (%s)", (127,))

    def The_difference(cr):

        cr.execute("SELECT ABS(my_rating - oppoenent_rating) FROM chess")

        

        result = cr.fetchall()

        for n in result:

            print(n)

    def ROUND_AND_TRANCAT(cr):

        cr.execute("SELECT ROUND(game_duration, 1), TRUNCATE(game_duration, 1) FROM chess")

        result = cr.fetchall()

        for n in result:

            print(f"ROUND : {n[0]}, TRUNCATE : {n[1]}")

    def ALTER(cr):

        cr.execute("ALTER TABLE chess CHANGE my_rating my_rating INT(4), CHANGE opponent_rating opponent_rating INT(4)")


    # Calling func :

    # DELTE(cr)

    # INSERT(cr)

    # ALTER(cr)

    The_difference(cr)

    ROUND_AND_TRANCAT(cr)

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:
        db.close()