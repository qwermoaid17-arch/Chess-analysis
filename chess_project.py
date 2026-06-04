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

    cr.execute("CREATE TABLE IF NOT EXISTS Chess_analysis(id INT AUTO_INCREMENT PRIMARY KEY, color_of_the_pieces ENUM('white', 'black'), opening_name VARCHAR(100), opponent_rating INT, your_rating INT, the_result ENUM('win', 'loss', 'draw'), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")


    def record_match(cr):
        while True:

            colore = input("Enter the color of the pieces: (1=> white, 2=> black 3=> back) ").strip().lower()

            if colore == "3" or colore == "back":
                break

            opening = input("Enter the opening name: ").strip().lower()

            if opening =="":

                opening = None
                    
            discount = int(input("Enter the discount evaluation: "))
            rating = int(input("Enter your rating: "))
            result = input("Enter the result (win, loss, draw): ")

            cr.execute("INSERT INTO Chess_analysis (color_of_the_pieces, opening_name, opponent_rating, your_rating, the_result) VALUES (%s, %s, %s, %s, %s)",
                    (colore, opening, discount, rating, result))
            
            break

    def show_win_mathes(cr):

            cr.execute("SELECT * FROM Chess_analysis WHERE the_result = 'win'")

            result = cr.fetchall()

            for n in result:

                print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}")


    def show_draw_mathes(cr):

        cr.execute("SELECT * FROM Chess_analysis WHERE the_result = 'draw'")

        result = cr.fetchall()

        for n in result:

            print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}")

    def show_loss_mathes(cr):

        cr.execute("SELECT * FROM Chess_analysis WHERE the_result = 'loss'")

        result = cr.fetchall()

        for n in result:

            print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}")

    def show_all_mathes(cr):

        cr.execute("SELECT * FROM Chess_analysis")

        result = cr.fetchall()

        for n in result:

            print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}")

    def search_matches(cr):

        while True:

            search = int(input("What are you looking for?:  (1=> color, 2=> opening 3=> your_rating 4=> opponent_rating 5=> result 6=> back) : "))

            if search == 6:

                break

            if search == 1:

                n_search = input("Enter the color: ").strip().lower()

                cr.execute("SELECT * FROM Chess_analysis WHERE color_of_the_pieces = %s", (n_search,))

            elif search == 2:

                n_search = input("Enter the opening name: ").strip().lower()

                if n_search.strip() == "":
                    
                    cr.execute("SELECT * FROM Chess_analysis ORDER BY opening_name DESC")

                    result = cr.fetchall()

                    for n in result:

                        if n[2] == None:

                            print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}")
                    # cr.execute("SELECT * FROM Chess_analysis WHERE opening_name is NULL")

                # else:

                    cr.execute("SELECT * FROM Chess_analysis WHERE opening_name = %s", (n_search,))

            elif search == 3:

                op = input("Do you want to search for ratings greater than, less than, or equal to a specific value? (Enter >, <, enter): ").strip()

                raw_input = int(input("Enter your rating (مثال: 800 أو >800 أو <1200): ").strip())

                if op == ">":

                    cr.execute("SELECT * FROM Chess_analysis ORDER BY your_rating DESC ")

                    result = cr.fetchall()

                    for n in result:

                        if n[3] > raw_input:

                            print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}")

                elif op == "<":

                    cr.execute("SELECT * FROM Chess_analysis ORDER BY your_rating ASC ")

                    result = cr.fetchall()

                    for n in result:

                        if n[3] < raw_input:

                            print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}")

                else:

                    cr.execute("SELECT * FROM Chess_analysis ORDER BY your_rating DESC ")

                    for n in cr.fetchall():

                            if n[3] == raw_input:

                                print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}")
            elif search == 4:

                op = input("Do you want to search for ratings greater than, less than, or equal to a specific value? (Enter >, <, enter): ").strip()

                raw_input = int(input("Enter your rating (مثال: 800 أو >800 أو <1200): ").strip())

                if op == ">":

                    cr.execute("SELECT * FROM Chess_analysis ORDER BY your_rating DESC ")

                    result = cr.fetchall()

                    for n in result:

                        if n[3] > raw_input:

                            print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}")

                elif op == "<":

                    cr.execute("SELECT * FROM Chess_analysis ORDER BY your_rating ASC ")

                    result = cr.fetchall()

                    for n in result:

                        if n[3] < raw_input:

                            print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}")

                else:

                    cr.execute("SELECT * FROM Chess_analysis ORDER BY your_rating DESC ")

                    for n in cr.fetchall():

                            if n[3] == raw_input:

                                print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}")
            break
    def update_match(cr):

        while True:

            match_id = int(input("Enter the ID of the match you want to update: (0=> back) "))

            if match_id == 0:

                break

            who_change = int(input("What do you want to change? (1 = color, 2 = opening, 3 = opponent_rating, 4 = your_rating, 5 = the_result): "))

            if who_change == 1:

                who_change = "color_of_the_pieces"

            elif who_change == 2:

                who_change = "opening_name"

            elif who_change == 3:

                who_change = "opponent_rating"
            
            elif who_change == 4:

                who_change = "your_rating"

            elif who_change == 5:

                who_change = "the_result"

            if who_change == "your_rating" or who_change == "opponent_rating":

                how_change = int(input("Enter the new value: "))

            else:

                how_change = input("Enter the new value: ")

            if who_change == "opening_name" and how_change.strip() == "":

                how_change = None

            cr.execute("UPDATE Chess_analysis SET " + who_change + " = %s WHERE id = %s", (how_change, match_id))

            break

    def DELETE_match(cr):
        while True:
            match_id = int(input("Enter the ID of the match you want to delete: (0=> back) "))

            if match_id == 0:
               
                break

            cr.execute("DELETE FROM Chess_analysis WHERE id = %s", (match_id,))

        print("Match deleted successfully")

    
    def show_day_mathes(cr):
            
            cr.execute("SELECT * FROM chess_analysis WHERE created_at >= CURDATE()")

            result = cr.fetchall()

            for n in result:

                print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}")

    def show_week_mathes(cr):

            cr.execute("SELECT * FROM chess_analysis WHERE YEARWEEK(created_at) = YEARWEEK(CURDATE())")

            result = cr.fetchall()

            for n in result:

                print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}")

    def show_month_mathes(cr):

            cr.execute("SELECT * FROM chess_analysis WHERE YEAR(created_at) = YEAR(CURDATE()) AND MONTH(created_at) = MONTH(CURDATE())")

            result = cr.fetchall()

            for n in result:

                print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}")

    info = """
    What do you want to do?
    1=> Record a new match
    2=> Statistics presentation and analysis
    3=> search for matches
    4=> UPDATE a match
    5=> Delete a match
    6=> Exit
    """

    while True:

        print(info)

        choice = int(input("Enter your choice: "))

        if choice == 6:

            print("Goodbye")

            break

        elif choice == 1:
            
            record_match(cr)

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

            h = """show what?
1=> DAY statistics
2=> WEEKLY statistics
3=> MONTHLY statistics
4=> Show all matches
5=> Show win matches
6=> Show draw matches
7=> Show loss matches
8=> Back to main menu"""
            
            print(h)

            Query = int(input("Enter your choice: "))


            while Query != 8:

                if Query == 1:

                    show_day_mathes(cr)

                    break

                elif Query == 2:

                    show_week_mathes(cr)

                    break

                elif Query == 3:

                    show_month_mathes(cr)

                    break

                if Query == 5:

                    show_win_mathes(cr)

                    break

                elif Query == 6:

                    show_draw_mathes(cr)

                    break
                
                elif Query == 7:

                    show_loss_mathes(cr)

                    break

                elif Query == 4:

                    show_all_mathes(cr)

                    break

        elif choice == 3:

            search_matches(cr)

        elif choice == 4:

            update_match(cr)


        elif choice == 5:
       
            DELETE_match(cr)

        db.commit()

except sql.Error as e:

    print(e)

finally:

    if db:

        db.close()
