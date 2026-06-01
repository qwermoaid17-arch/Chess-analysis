import pymysql as sql



try:

    db = sql.connect(
        host = "localhost",
        user = "root",
        password = "",
        charset='utf8mb4'
    )

    cr = db.cursor()

    cr.execute("CREATE DATABASE IF NOT EXISTS Chess")

    cr.execute("USE Chess")

    cr.execute("CREATE TABLE IF NOT EXISTS Chess_analysis(id INT AUTO_INCREMENT PRIMARY KEY, color_of_the_pieces ENUM('white', 'black'), opening_name VARCHAR(100), opponent_rating INT, your_rating INT, the_result ENUM('win', 'loss', 'draw'))")

    info = """
    What do you want to do?
    1=> Record a new match
    2=> Statistics presentation and analysis
    3=> Delete a match
    4=> Exit
    """

    while True:

        print(info)

        choice = int(input("Enter your choice: "))

        if choice == 4:

            print("Goodbye")

            break

        elif choice == 1:
            
            colore = input("Enter the color of the pieces: ")
            opening = input("Enter the opening name: ")
            discount = int(input("Enter the discount evaluation: "))
            rating = int(input("Enter your rating: "))
            result = input("Enter the result (win, loss, draw): ")

            cr.execute("INSERT INTO Chess_analysis (color_of_the_pieces, opening_name, opponent_rating, your_rating, the_result) VALUES (%s, %s, %s, %s, %s)",
                        (colore, opening, discount, rating, result))
        
        elif choice == 2:

            cr.execute("SELECT count(id) FROM Chess_analysis")

            result = cr.fetchall()

            for n in result:

                print(f" Number of matches played: {n[0]}")

            cr.execute("SELECT count(id) FROM Chess_analysis WHERE the_result = 'win'")

            result = cr.fetchall()

            for n in result:

                print(f" Number of matches won: {n[0]}")

            cr.execute("SELECT count(id) FROM Chess_analysis WHERE the_result = 'loss'")

            result = cr.fetchall()

            for n in result:

                print(f" Number of matches lost: {n[0]}")

            cr.execute("SELECT  count(id) FROM Chess_analysis WHERE the_result = 'draw'")

            result = cr.fetchall()

            for n in result:

                print(f" Number of matches drawn: {n[0]}")

            cr.execute("SELECT AVG(opponent_rating) FROM Chess_analysis")

            result = cr.fetchall()

            for n in result:

                print(f" Average discount evaluation: {n[0]}")

            cr.execute("SELECT opening_name, count(*) AS counted FROM Chess_analysis WHERE the_result = %s GROUP BY opening_name ORDER BY counted DESC LIMIT 1", ('win',))

            result = cr.fetchall()

            for n in result:

                print(f" The opening match saw many wins.: {n[0]}")

            cr.execute("SELECT color_of_the_pieces, count(*) AS counted FROM Chess_analysis WHERE the_result = %s GROUP BY color_of_the_pieces ORDER BY counted DESC LIMIT 1", ('win',))

            result = cr.fetchall()

            for n in result:

                print(f" The color I won with the most: {n[0]}")

            cr.execute("SELECT MAX(your_rating) FROM Chess_analysis")

            result = cr.fetchall()

            for n in result:

                print(f" Max your rating: {n[0]}")

        elif choice == 3:
       
            cr.execute("DELETE FROM Chess_analysis WHERE id = %s", (int(input("Enter ID: ")),))

            print("Match deleted successfully")

        db.commit()

except sql.Error as e:

    print(e)

finally:

    if db:

        db.close()
