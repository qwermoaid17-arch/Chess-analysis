import pymysql as sql


db = None

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

    def check_int_First_list(value):
        
        try:
        
            value = int(value)

            if value > 5 or value < 0:

                print("Invalid input. Please enter a number between 0 and 5.")

                return False

            return True

        
        except ValueError:

            print('Invalid input. Please enter an integer.')

            return False
        
    def check_int_list_two(value):

        try:

            if value == "#":

                return value
             
            
            else:

                value = int(value)

                return True


        except ValueError:

            print('Invalid input. Please enter an integer.')

            return False
        
    def check_int_list(value):

        try:

            if value == "#":

                return value
            
            if value == "*":

                return value
             
            
            else:

                value = int(value)

                return True


        except ValueError:

            print('Invalid input. Please enter an integer.')

            return False
        
        
    # def check_int_update(value):

    #     try:

    #         if value == "#":

    #             return value
             
            
    #         else:

    #             value = int(value)

    #             return True


    #     except ValueError:

    #         print('Invalid input. Please enter an integer.')

    #         return False
        

        


        
    def check_int_show(value):
        
        try:


        

            value = int(value)

            if value > 8 or value < 0:

                print("Invalid input. Please enter a number between 0 and 7.")

                return False

            return True

        
        except ValueError:

            print('Invalid input. Please enter an integer.')

            return False
        
    def check_int_search(value):
        
        try:

            value = int(value)

            return True

        
        except ValueError:

            print('Invalid input. Please enter an integer.')

            return False
        
    # def check_int_search(value):
        
    #     try:


        

    #         value = int(value)

    #         return True

        
    #     except ValueError:

    #         print('Invalid input. Please enter an integer.')

    #         return False
        


    def record_match(cr):
        
        step = 1

        while True:



            if step == 1:
                    
                while True:

                    colore = input("Enter the color of the pieces: (1=> white, 2=> black, * => exit) ").strip().lower()

                    if colore == '*':

                        step = 7

                        break

                    elif colore == "1" or colore == "2":

                        step = 2

                        break

                    elif colore != "1" and colore != "2":

                        print("Invalid input. Please enter 1 or 2.")

                        continue

                    else:

                        step = 2

            elif step == 2:

                while True:

                    opening = input("Enter the opening name (#=> back, * => exit): ").strip().lower()

                    if opening =="":

                        opening = None

                        step = 3

                        break

                    elif opening == "#":

                        step = 1

                        break

                    elif opening == '*':

                        print("Goodbye")

                        step = 7

                        break

                    else:

                        step = 3

                        break

            elif step == 3:

                while True:

                    discount = input("Enter the discount evaluation (#=> back, * => exit) :")

                    if check_int_list(discount) == "#":

                        step = 2 

                        break

                    elif check_int_list(discount) == False:

                        continue

                    elif check_int_list(discount) == '*':

                        print("Goodbye")

                        step = 7

                        break

                    else:

                        discount = int(discount)
                        
                        step = 4
                        
                        break

            elif step == 4:

                while True:

                    rating = input("Enter your rating (#=> back, * => exit): ")

                    if check_int_list(rating) == "#":

                        step = 3

                        break

                    elif check_int_list(rating) == '*':

                        print("Goodbye")

                        step = 7

                        break

                    elif check_int_list(rating) == False:

                        continue
                

                    else:

                        rating = int(rating)

                        step = 5

                        break



            elif step == 5:

                while True:


                    result = input("Enter the result (1=> win, 2=> loss, 3=> draw #=> back, * => exit): ")

                    if result == "#":

                        step = 4

                        break

                    elif result == '*':

                        print("Goodbye")

                        step = 7

                        break

                    else:

                        step = 6

                        break

            elif step == 6:


                cr.execute("INSERT INTO Chess_analysis (color_of_the_pieces, opening_name, opponent_rating, your_rating, the_result) VALUES (%s, %s, %s, %s, %s)",
                        (colore, opening, discount, rating, result))
                
                step = 7
                    


            elif step == 7:

                db.commit()

                print("Match recorded successfully.")

                break


    def show_analysis(cr):
            
        cr.execute("SELECT count(id) FROM Chess_analysis")

        result = cr.fetchall()

        for n in result:

            print(f" Number of matches played: {n[0]}")

        cr.execute("SELECT count(CASE WHEN the_result = 'win' THEN 1 END) as counted,count(CASE WHEN the_result = 'win' THEN 1 END) / count(*) * 100 FROM Chess_analysis")

        result = cr.fetchall()

        for n in result:

            print(f" Number of matches won: {n[0]} | Percentage: {n[1]}%")

        cr.execute("SELECT count(CASE WHEN the_result = 'loss' THEN 1 END) as counted, count(CASE WHEN the_result = 'loss' THEN 1 END) / count(*) * 100 FROM Chess_analysis ")

        result = cr.fetchall()

        for n in result:

            print(f" Number of matches lost: {n[0]} | prcentage: {n[1]}%")

        cr.execute("SELECT count(CASE WHEN the_result = 'draw' THEN 1 END) as counted, count(CASE WHEN the_result = 'draw' THEN 1 END) / count(*) * 100 FROM Chess_analysis ")

        result = cr.fetchall()

        for n in result:

            print(f" Number of matches drawn: {n[0]} | prcentage: {n[1]}%")

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

        cr.execute("SELECT COUNT(CASE WHEN color_of_the_pieces = 'white' and the_result = 'win' THEN 1 END) AS counted, COUNT(CASE WHEN color_of_the_pieces = 'white' and the_result = 'win' THEN 1 END) / COUNT(*) * 100 AS win_percentage, " \
        " COUNT(CASE WHEN color_of_the_pieces = 'white' and the_result = 'draw' THEN 1 END ) as casese, COUNT(CASE WHEN color_of_the_pieces = 'white' and the_result = 'draw' THEN 1 END ) / COUNT(*) * 100 as draw_percentage, " \
        " COUNT(CASE WHEN color_of_the_pieces = 'White' and the_result = 'loss' THEN 1 END ) as cased, COUNT(CASE WHEN color_of_the_pieces = 'White' and the_result = 'loss' THEN 1 END ) / COUNT(*) * 100 as loss_percentage FROM Chess_analysis")

        for n in cr.fetchall():

            print(f"won white : {n[0]} , win_white_percentage : {n[1]} % , draw white : {n[2]} , draw_white_percentage : {n[3]} % ,  loss white : {n[4]} , loss_white_percentage : {n[5]} %")

        cr.execute("SELECT COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'win' THEN 1 END) AS counted, COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'win' THEN 1 END) / COUNT(*) * 100 AS win_percentage, " \
        " COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'draw' THEN 1 END ) as casese, COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'draw' THEN 1 END ) / COUNT(*) * 100 as draw_percentage, " \
        " COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'loss' THEN 1 END ) as cased, COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'loss' THEN 1 END ) / COUNT(*) * 100 as loss_percentage FROM Chess_analysis")

        for n in cr.fetchall():

            print(f" won black : {n[0]} , win_black_percentage : {n[1]} % , draw black : {n[2]} , draw_black_percentage : {n[3]} % ,  loss black : {n[4]} , loss_black_percentage : {n[5]} %")



        cr.execute("SELECT MAX(your_rating) FROM Chess_analysis")

        result = cr.fetchall()

        for n in result:

            print(f" Max your rating: {n[0]}")


            

        while True:

            h = """show what?
1=> DAY statistics
2=> WEEKLY statistics
3=> MONTHLY statistics
4=> Show all matches
5=> Show win matches
6=> Show draw matches
7=> Show loss matches
8=> Show the best hour
0=> Back to main menu"""

            print(h)
            Query = input("Enter your choice: ")

            if check_int_show(Query) == False:

                continue

            else:

                Query = int(Query)

            if Query == 0:

                print("Goodbye")

                break

            # while Query != 0:

            if Query == 1:

                show_day_analysis(cr)

                    # break

            elif Query == 2:

                show_week_analysis(cr)

                    # break

            elif Query == 3:

                show_month_analysis(cr)

                    # break

            elif Query == 5:

                show_win_mathes(cr)

                    # break

            elif Query == 6:

                show_draw_mathes(cr)

                    # break
                    
            elif Query == 7:

                show_loss_mathes(cr)

                    # break

            elif Query == 4:

                show_all_mathes(cr)

                    # break

            elif Query == 8:

                show_clock_best(cr)

                    # break

            else :

                print("Invalid choice. Please try again.")

             
                    
    def show_win_mathes(cr):

            cr.execute("SELECT *  , CONCAT('played ', DATEDIFF(CURDATE(), created_at), ' days ago') AS cancated FROM Chess_analysis WHERE the_result = 'win'")

            result = cr.fetchall()

            for n in result:

                print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}, {n[7]}")

    def show_draw_mathes(cr):

        cr.execute("SELECT * ,CONCAT('played ', DATEDIFF(CURDATE(), created_at), ' days ago') AS cancated FROM Chess_analysis WHERE the_result = 'draw'")

        result = cr.fetchall()

        for n in result:

            print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}, {n[7]}")

    def show_loss_mathes(cr):

        cr.execute("SELECT * , CONCAT('played ', DATEDIFF(CURDATE(), created_at), ' days ago') AS cancated FROM Chess_analysis WHERE the_result = 'loss'")

        result = cr.fetchall()

        for n in result:

            print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}, {n[7]}")

    def show_all_mathes(cr):

        cr.execute("SELECT * , CONCAT('played ', DATEDIFF(CURDATE(), created_at), ' days ago') AS cancated FROM Chess_analysis")

        result = cr.fetchall()

        for n in result:

            print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}, {n[7]}")

    def search_matches(cr):

        while True:

            search = input("What are you looking for?:  (1=> color, 2=> opening 3=> your_rating 4=> opponent_rating 5=> result 0=> back) : ")

            if check_int_search(search) == False:

                continue

            else:

                search = int(search)

            if search == 0:

                break



            if search == 1:
                    
                while True:

                    n_search = input("Enter the color (1=> white, 2=> black 0=> back): ").strip().lower()

                    if n_search == '0':

                        break



                    if n_search == "1":

                        n_search = "white"

                    elif n_search == "2":

                        n_search = "black"

                    else:

                        print("Invalid choice. Please try again.")

                        continue

                    break

                cr.execute("SELECT * , CONCAT('played ', DATEDIFF(CURDATE(), created_at), ' days ago') AS cancated FROM Chess_analysis WHERE color_of_the_pieces = %s", (n_search,))

                result = cr.fetchall()

                for n in result:

                    print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}, {n[7]}")
                    


            elif search == 2:

                while True:

                    n_search = input("Enter the opening name (0=> back): ").strip().lower()

                    if n_search == "0":

                        break

                    break

                if n_search.strip() == "":
                    
                    cr.execute("SELECT * , CONCAT('played ', DATEDIFF(CURDATE(), created_at), ' days ago') AS cancated FROM Chess_analysis ORDER BY opening_name DESC")

                    result = cr.fetchall()

                    for n in result:

                        if n[2] == None:

                            print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}, {n[7]}")
                    # cr.execute("SELECT * FROM Chess_analysis WHERE opening_name is NULL")

                # else:

                    cr.execute("SELECT * FROM Chess_analysis WHERE opening_name = %s", (n_search,))

                    result = cr.fetchall()

                    for n in result:

                        print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}, {n[7]}")

            elif search == 3:

                while True:

                    op = input("Do you want to search for ratings greater than, less than, or equal to a specific value? (Enter >, <, =, # => back): ").strip()

                    if op == "#":

                        break

                    
                    while True:

                        raw_input =input("Enter your rating (# => back)): ").strip()

                        if raw_input == '#':

                            break
                            
                        else:

                            raw_input = int(raw_input)

                                    

                        break

                    if raw_input == '#':

                        break

                    if op == ">":

                        # cr.execute("SELECT * , CONCAT('played ', DATEDIFF(CURDATE(), created_at), ' days ago') AS cancated FROM Chess_analysis ORDER BY your_rating DESC ")

                        # result = cr.fetchall()

                        # for n in result:

                        #     if n[3] > raw_input:

                        cr.execute("SELECT *, CONCAT('played ', DATEDIFF(CURDATE(), created_at), ' days ago') AS cancated FROM Chess_analysis WHERE your_rating > %s ORDER BY your_rating DESC ", (raw_input,))

                        result = cr.fetchall()

                        for n in result:

                                print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}, {n[7]}")

                    elif op == "<":

                        cr.execute("SELECT * , CONCAT('played ', DATEDIFF(CURDATE(), created_at), ' days ago') AS cancated FROM Chess_analysis WHERE your_rating < %s ORDER BY your_rating DESC ", (raw_input,))

                        result = cr.fetchall()

                        for n in result:

                                print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}, {n[7]}")

                    elif op == "=":

                        cr.execute("SELECT * , CONCAT('played ', DATEDIFF(CURDATE(), created_at), ' days ago') AS cancated FROM Chess_analysis WHERE your_rating = %s", (raw_input,))

                        for n in cr.fetchall():
                    
                                    print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}, {n[7]}")

                                    
            elif search == 4:

                while True:

                    op = input("Do you want to search for ratings greater than, less than, or equal to a specific value? (Enter >, <, =, #=> back): ").strip()

                    if op == "#":

                        break

                    while True:

                        raw_input = input("Enter your rating (#=> back)): ").strip()

                        if raw_input == '#':

                            break

                        else:

                            raw_input = int(raw_input)
                            
                                    

                        break

                    if raw_input == '#':

                        break

                    if op == ">":

                        cr.execute("SELECT *, CONCAT('played ', DATEDIFF(CURDATE(), created_at), ' days ago') AS cancated FROM Chess_analysis WHERE opponent_rating > %s ORDER BY opponent_rating DESC ", (raw_input,))

                        result = cr.fetchall()

                        for n in result:


                                print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}, {n[7]}")

                    elif op == "<":

                        cr.execute("SELECT * , CONCAT('played ', DATEDIFF(CURDATE(), created_at), ' days ago') AS cancated FROM Chess_analysis WHERE opponent_rating < %s ORDER BY opponent_rating DESC ", (raw_input,))

                        result = cr.fetchall()

                        for n in result:

                            if n[3] < raw_input:

                                print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}, {n[7]}")

                    elif op == "=":

                        cr.execute("SELECT * , CONCAT('played ', DATEDIFF(CURDATE(), created_at), ' days ago') AS cancated FROM Chess_analysis WHERE opponent_rating = %s", (raw_input,))


                        for n in cr.fetchall():

                                if n[3] == raw_input:

                                    print(f"ID: {n[0]}, Color: {n[1]}, Opening: {n[2]}, Opponent Rating: {n[3]}, Your Rating: {n[4]}, Result: {n[5]}, {n[7]}")

    def update_match(cr):

        while True:

            step = 1

            match_id = input("Enter the ID of the match you want to update: (0=> back) ")

            if check_int_list_two(match_id) == False:

                continue

            elif match_id == "0":

                break

            else:

                match_id = int(match_id)

            while True:

                if step == 1 :

                    who_change = input("What do you want to change? (1 = color, 2 = opening, 3 = opponent_rating, 4 = your_rating, 5 = the_resultm (0=> back): ")

                    if check_int_list_two(who_change) == False:

                        continue

                    elif who_change == 0:

                        break

                    else:

                        who_change = int(who_change)

                    step = 2

                    break

            if who_change == 0:

                break

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

            if who_change == "your_rating":

                while True:

                    how_change = input("Enter the new your rating (#=> back): ")

                    if check_int_list_two(how_change) == False:

                        continue

                    elif how_change == "#":

                        step = 1

                    else:

                        how_change = int(how_change)

                    break

            elif who_change == "opponent_rating":

                while True:

                    how_change = input("Enter the new opponent rating (#=> back): ")

                    if check_int_list_two(how_change) == False:

                        continue

                    elif how_change == "#":

                        step = 1

                    else:

                        how_change = int(how_change)

                    break

            elif who_change == "color_of_the_pieces" :

                while True:

                    how_change = input("Enter the new color (1=> white, 2=> black, (#=> back): ")

                    if how_change == "#":
                        
                        step = 1

                        break

                    else :

                        break

            elif who_change == "opening_name" :

                while True:

                    how_change = input("Enter the new opening (#=> back): ")

                    if how_change == "#":
                        
                        step = 1

                        break

                    else:

                        break

            elif who_change == "the_result" :

                while True:

                    how_change = input("Enter the new result (#=> back): ")

                    if how_change == "#":
                        
                        step = 1

                        break

                    else:

                        break

            

            if who_change == "opening_name" and how_change.strip() == "":

                how_change = None

            cr.execute("UPDATE Chess_analysis SET " + who_change + " = %s WHERE id = %s", (how_change, match_id))

            db.commit()

            print("Match updated successfully")




    def DELETE_match(cr):
        while True:
            
            match_id = input("Enter the ID of the match you want to delete: (0=> back) ")

            if check_int_search(match_id) == False:

                continue

            elif match_id == "0":

                break

            else:

                match_id = int(match_id)

            cr.execute("DELETE FROM Chess_analysis WHERE id = %s", (match_id,))

            db.commit()

        print("Match deleted successfully")

    
    def show_day_analysis(cr):


        cr.execute("SELECT count(id) FROM Chess_analysis WHERE DATE(created_at) = CURDATE()")

        result = cr.fetchall()

        for n in result:

            print(f" Number of matches played: {n[0]}")

        cr.execute("SELECT count(CASE WHEN the_result = 'win' THEN 1 END) as counted,count(CASE WHEN the_result = 'win' THEN 1 END) / count(*) * 100 FROM Chess_analysis WHERE DATE(created_at) = CURDATE()")

        result = cr.fetchall()

        for n in result:

            print(f" Number of matches won: {n[0]} | Percentage: {n[1]}%")

        cr.execute("SELECT count(CASE WHEN the_result = 'loss' THEN 1 END) as counted, count(CASE WHEN the_result = 'loss' THEN 1 END) / count(*) * 100 FROM Chess_analysis WHERE DATE(created_at) = CURDATE()")

        result = cr.fetchall()

        for n in result:

            print(f" Number of matches lost: {n[0]} | prcentage: {n[1]}%")

        cr.execute("SELECT count(CASE WHEN the_result = 'draw' THEN 1 END) as counted, count(CASE WHEN the_result = 'draw' THEN 1 END) / count(*) * 100 FROM Chess_analysis WHERE DATE(created_at) = CURDATE()")

        result = cr.fetchall()

        for n in result:

            print(f" Number of matches drawn: {n[0]} | prcentage: {n[1]}%")

        cr.execute("SELECT AVG(opponent_rating) FROM Chess_analysis WHERE DATE(created_at) = CURDATE()")

        result = cr.fetchall()

        for n in result:

            print(f" Average discount evaluation: {n[0]}")

        cr.execute("SELECT opening_name, count(*) AS counted FROM Chess_analysis WHERE the_result = %s and DATE(created_at) = CURDATE() GROUP BY opening_name ORDER BY counted DESC LIMIT 1", ('win',))

        result = cr.fetchall()

        for n in result:

            print(f" The opening match saw many wins.: {n[0]}")

        cr.execute("SELECT color_of_the_pieces, count(*) AS counted FROM Chess_analysis WHERE the_result = %s and DATE(created_at) = CURDATE() GROUP BY color_of_the_pieces ORDER BY counted DESC LIMIT 1", ('win',))

        result = cr.fetchall()

        for n in result:

            print(f" The color I won with the most: {n[0]}")

        cr.execute("SELECT COUNT(CASE WHEN color_of_the_pieces = 'white' and the_result = 'win' THEN 1 END) AS counted, COUNT(CASE WHEN color_of_the_pieces = 'white' and the_result = 'win' THEN 1 END) / COUNT(*) * 100 AS win_percentage, " \
        " COUNT(CASE WHEN color_of_the_pieces = 'white' and the_result = 'draw' THEN 1 END ) as casese, COUNT(CASE WHEN color_of_the_pieces = 'white' and the_result = 'draw' THEN 1 END ) / COUNT(*) * 100 as draw_percentage, " \
        " COUNT(CASE WHEN color_of_the_pieces = 'White' and the_result = 'loss' THEN 1 END ) as cased, COUNT(CASE WHEN color_of_the_pieces = 'White' and the_result = 'loss' THEN 1 END ) / COUNT(*) * 100 as loss_percentage FROM Chess_analysis WHERE DATE(created_at) = CURDATE()")

        for n in cr.fetchall():

            print(f"won white : {n[0]} , win_white_percentage : {n[1]} % , draw white : {n[2]} , draw_white_percentage : {n[3]} % ,  loss white : {n[4]} , loss_white_percentage : {n[5]} %")

        cr.execute("SELECT COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'win' THEN 1 END) AS counted, COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'win' THEN 1 END) / COUNT(*) * 100 AS win_percentage, " \
        " COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'draw' THEN 1 END ) as casese, COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'draw' THEN 1 END ) / COUNT(*) * 100 as draw_percentage, " \
        " COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'loss' THEN 1 END ) as cased, COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'loss' THEN 1 END ) / COUNT(*) * 100 as loss_percentage FROM Chess_analysis WHERE DATE(created_at) = CURDATE()")

        for n in cr.fetchall():

            print(f" won black : {n[0]} , win_black_percentage : {n[1]} % , draw black : {n[2]} , draw_black_percentage : {n[3]} % ,  loss black : {n[4]} , loss_black_percentage : {n[5]} %")



        cr.execute("SELECT MAX(your_rating) FROM Chess_analysis  WHERE DATE(created_at) = CURDATE()")

        result = cr.fetchall()

        for n in result:

            print(f" Max your rating: {n[0]}")




    def show_month_analysis(cr):

        cr.execute("SELECT count(id) FROM Chess_analysis WHERE MONTH(created_at) = MONTH(CURDATE()) AND YEAR(created_at) = YEAR(CURDATE())")

        result = cr.fetchall()

        for n in result:

            print(f" Number of matches played: {n[0]}")

        cr.execute("SELECT count(CASE WHEN the_result = 'win' THEN 1 END) as counted,count(CASE WHEN the_result = 'win' THEN 1 END) / count(*) * 100 FROM Chess_analysis WHERE MONTH(created_at) = MONTH(CURDATE()) AND YEAR(created_at) = YEAR(CURDATE())")

        result = cr.fetchall()

        for n in result:

            print(f" Number of matches won: {n[0]} | Percentage: {n[1]}%")

        cr.execute("SELECT count(CASE WHEN the_result = 'loss' THEN 1 END) as counted, count(CASE WHEN the_result = 'loss' THEN 1 END) / count(*) * 100 FROM Chess_analysis WHERE MONTH(created_at) = MONTH(CURDATE()) AND YEAR(created_at) = YEAR(CURDATE()) ")

        result = cr.fetchall()

        for n in result:

            print(f" Number of matches lost: {n[0]} | prcentage: {n[1]}%")

        cr.execute("SELECT count(CASE WHEN the_result = 'draw' THEN 1 END) as counted, count(CASE WHEN the_result = 'draw' THEN 1 END) / count(*) * 100 FROM Chess_analysis WHERE MONTH(created_at) = MONTH(CURDATE()) AND YEAR(created_at) = YEAR(CURDATE()) ")

        result = cr.fetchall()

        for n in result:

            print(f" Number of matches drawn: {n[0]} | prcentage: {n[1]}%")

        cr.execute("SELECT AVG(opponent_rating) FROM Chess_analysis WHERE MONTH(created_at) = MONTH(CURDATE()) AND YEAR(created_at) = YEAR(CURDATE())")

        result = cr.fetchall()

        for n in result:

            print(f" Average discount evaluation: {n[0]}")

        cr.execute("SELECT opening_name, count(*) AS counted FROM Chess_analysis WHERE the_result = %s and MONTH(created_at) = MONTH(CURDATE()) AND YEAR(created_at) = YEAR(CURDATE()) GROUP BY opening_name ORDER BY counted DESC LIMIT 1", ('win',))

        result = cr.fetchall()

        for n in result:

            print(f" The opening match saw many wins.: {n[0]}")

        cr.execute("SELECT color_of_the_pieces, count(*) AS counted FROM Chess_analysis WHERE the_result = %s and MONTH(created_at) = MONTH(created_at)and YEAR(created_at) = YEAR(CURDATE()) GROUP BY color_of_the_pieces ORDER BY counted DESC LIMIT 1", ('win',))

        result = cr.fetchall()

        for n in result:

            print(f" The color I won with the most: {n[0]}")

        cr.execute("SELECT COUNT(CASE WHEN color_of_the_pieces = 'white' and the_result = 'win' THEN 1 END) AS counted, COUNT(CASE WHEN color_of_the_pieces = 'white' and the_result = 'win' THEN 1 END) / COUNT(*) * 100 AS win_percentage, " \
        " COUNT(CASE WHEN color_of_the_pieces = 'white' and the_result = 'draw' THEN 1 END ) as casese, COUNT(CASE WHEN color_of_the_pieces = 'white' and the_result = 'draw' THEN 1 END ) / COUNT(*) * 100 as draw_percentage, " \
        " COUNT(CASE WHEN color_of_the_pieces = 'White' and the_result = 'loss' THEN 1 END ) as cased, COUNT(CASE WHEN color_of_the_pieces = 'White' and the_result = 'loss' THEN 1 END ) / COUNT(*) * 100 as loss_percentage FROM Chess_analysis WHERE MONTH(created_at) = MONTH(CURDATE()) AND YEAR(created_at) = YEAR(CURDATE())")

        for n in cr.fetchall():

            print(f"won white : {n[0]} , win_white_percentage : {n[1]} % , draw white : {n[2]} , draw_white_percentage : {n[3]} % ,  loss white : {n[4]} , loss_white_percentage : {n[5]} %")

        cr.execute("SELECT COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'win' THEN 1 END) AS counted, COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'win' THEN 1 END) / COUNT(*) * 100 AS win_percentage, " \
        " COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'draw' THEN 1 END ) as casese, COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'draw' THEN 1 END ) / COUNT(*) * 100 as draw_percentage, " \
        " COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'loss' THEN 1 END ) as cased, COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'loss' THEN 1 END ) / COUNT(*) * 100 as loss_percentage FROM Chess_analysis WHERE MONTH(created_at) = MONTH(CURDATE()) AND YEAR(created_at) = YEAR(CURDATE())")

        for n in cr.fetchall():

            print(f" won black : {n[0]} , win_black_percentage : {n[1]} % , draw black : {n[2]} , draw_black_percentage : {n[3]} % ,  loss black : {n[4]} , loss_black_percentage : {n[5]} %")



        cr.execute("SELECT MAX(your_rating) FROM Chess_analysis  WHERE MONTH(created_at) = MONTH(created_at) AND YEAR(created_at) = YEAR(CURDATE())")

        result = cr.fetchall()

        for n in result:

            print(f" Max your rating: {n[0]}")



    def show_week_analysis(cr):

        cr.execute("SELECT count(id) FROM Chess_analysis WHERE YEARWEEK(created_at) = YEARWEEK(CURDATE())")

        result = cr.fetchall()

        for n in result:

            print(f" Number of matches played: {n[0]}")

        cr.execute("SELECT count(CASE WHEN the_result = 'win' THEN 1 END) as counted,count(CASE WHEN the_result = 'win' THEN 1 END) / count(*) * 100 FROM Chess_analysis WHERE YEARWEEK(created_at) = YEARWEEK(CURDATE(), 0)")

        result = cr.fetchall()

        for n in result:

            print(f" Number of matches won: {n[0]} | Percentage: {n[1]}%")

        cr.execute("SELECT count(CASE WHEN the_result = 'loss' THEN 1 END) as counted, count(CASE WHEN the_result = 'loss' THEN 1 END) / count(*) * 100 FROM Chess_analysis WHERE YEARWEEK(created_at) = YEARWEEK(CURDATE(), 0) ")

        result = cr.fetchall()

        for n in result:

            print(f" Number of matches lost: {n[0]} | prcentage: {n[1]}%")

        cr.execute("SELECT count(CASE WHEN the_result = 'draw' THEN 1 END) as counted, count(CASE WHEN the_result = 'draw' THEN 1 END) / count(*) * 100 FROM Chess_analysis WHERE YEARWEEK(created_at) = YEARWEEK(CURDATE()) ")

        result = cr.fetchall()

        for n in result:

            print(f" Number of matches drawn: {n[0]} | prcentage: {n[1]}%")

        cr.execute("SELECT AVG(opponent_rating) FROM Chess_analysis WHERE YEARWEEK(created_at) = YEARWEEK(CURDATE())")

        result = cr.fetchall()

        for n in result:

            print(f" Average discount evaluation: {n[0]}")

        cr.execute("SELECT opening_name, count(*) AS counted FROM Chess_analysis WHERE the_result = %s and YEARWEEK(created_at) = YEARWEEK(CURDATE()) GROUP BY opening_name ORDER BY counted DESC LIMIT 1", ('win',))

        result = cr.fetchall()

        for n in result:

            print(f" The opening match saw many wins.: {n[0]}")

        cr.execute("SELECT color_of_the_pieces, count(*) AS counted FROM Chess_analysis WHERE the_result = %s and YEARWEEK(created_at) = YEARWEEK(CURDATE()) GROUP BY color_of_the_pieces ORDER BY counted DESC LIMIT 1", ('win',))

        result = cr.fetchall()

        for n in result:

            print(f" The color I won with the most: {n[0]}")

        cr.execute("SELECT COUNT(CASE WHEN color_of_the_pieces = 'white' and the_result = 'win' THEN 1 END) AS counted, COUNT(CASE WHEN color_of_the_pieces = 'white' and the_result = 'win' THEN 1 END) / COUNT(*) * 100 AS win_percentage, " \
        " COUNT(CASE WHEN color_of_the_pieces = 'white' and the_result = 'draw' THEN 1 END ) as casese, COUNT(CASE WHEN color_of_the_pieces = 'white' and the_result = 'draw' THEN 1 END ) / COUNT(*) * 100 as draw_percentage, " \
        " COUNT(CASE WHEN color_of_the_pieces = 'White' and the_result = 'loss' THEN 1 END ) as cased, COUNT(CASE WHEN color_of_the_pieces = 'White' and the_result = 'loss' THEN 1 END ) / COUNT(*) * 100 as loss_percentage FROM Chess_analysis WHERE YEARWEEK(created_at) = YEARWEEK(CURDATE())")

        for n in cr.fetchall():

            print(f"won white : {n[0]} , win_white_percentage : {n[1]} % , draw white : {n[2]} , draw_white_percentage : {n[3]} % ,  loss white : {n[4]} , loss_white_percentage : {n[5]} %")

        cr.execute("SELECT COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'win' THEN 1 END) AS counted, COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'win' THEN 1 END) / COUNT(*) * 100 AS win_percentage, " \
        " COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'draw' THEN 1 END ) as casese, COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'draw' THEN 1 END ) / COUNT(*) * 100 as draw_percentage, " \
        " COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'loss' THEN 1 END ) as cased, COUNT(CASE WHEN color_of_the_pieces = 'black' and the_result = 'loss' THEN 1 END ) / COUNT(*) * 100 as loss_percentage FROM Chess_analysis WHERE YEARWEEK(created_at) = YEARWEEK(CURDATE())")

        for n in cr.fetchall():

            print(f" won black : {n[0]} , win_black_percentage : {n[1]} % , draw black : {n[2]} , draw_black_percentage : {n[3]} % ,  loss black : {n[4]} , loss_black_percentage : {n[5]} %")



        cr.execute("SELECT MAX(your_rating) FROM Chess_analysis  WHERE YEARWEEK(created_at) = YEARWEEK(CURDATE())")

        result = cr.fetchall()

        for n in result:

            print(f" Max your rating: {n[0]}")

    def show_clock_best(cr):

        cr.execute("SELECT HOUR(created_at) AS HOURED , count(*) FROM chess_analysis WHERE the_result = 'win' GROUP BY HOURED ORDER BY count(*) DESC LIMIT 1")

        for row in cr.fetchall():

            print(f"The best time to win is {row[0]} hours")

    info = """
    What do you want to do?
    1=> Record a new match
    2=> Statistics presentation and analysis
    3=> search for matches
    4=> UPDATE a match
    5=> Delete a match
    0=> Exit
    """

    while True:

        print(info)

        choice = input("Enter your choice: ")

        if check_int_First_list(choice) == False:

            continue
        else:

            choice = int(choice)

        if choice == 0:

            print("Goodbye")

            break

        elif choice == 1:
            
            record_match(cr)

        elif choice == 2:

            show_analysis(cr)

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
