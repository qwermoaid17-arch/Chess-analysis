import pymysql as sql

try:

    db = sql.connect(

        host = "localhost",
        user = "root",
        passwd="",
        charset="utf8mb4"
    )

    cr = db.cursor()

    cr.execute("CREATE DATABASE IF NOT EXISTS library_db")

    cr.execute("USE library_db")

    # cr.execute("DROP TABLE books")

    cr.execute("CREATE TABLE IF NOT EXISTS books(books_id INT AUTO_INCREMENT PRIMARY KEY, isbn VARCHAR(20) NOT NULL UNIQUE, title VARCHAR(255) NOT NULL, auther VARCHAR(255) NOT NULL)")

    # cr.execute("INSERT INTO  books(isbn, title, auther) VALUES(%s, %s, %s)", ('978-0132350884', 'night', 'today'))

    # cr.execute("INSERT INTO  books(isbn, title, auther) VALUES(%s, %s, %s)", ('978-0596005658', 'learning python', 'today'))
    #error
    cr.execute("INSERT INTO  books(isbn, title, auther) VALUES(%s, %s, %s)", ('978-0132350884', 'night', 'today'))



    db.commit()

    db.close()


except sql.Error as er:

    print("error", er)