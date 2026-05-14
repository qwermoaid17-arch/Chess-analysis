import pymysql as sql

try:

    db = sql.connect(
        host = "localhost",
        user = "root",
        password = "",
        charset='utf8mb4'
    )

    cr = db.cursor()

    cr.execute("CREATE DATABASE IF NOT EXISTS Constraints")

    cr.execute("USE Constraints")

    cr.execute("CREATE TABLE IF NOT EXISTS father (id INT NOT NULL PRIMARY KEY, username VARCHAR(100) UNIQUE, email VARCHAR(255) NOT NULL UNIQUE)")

    cr.execute("CREATE TABLE IF NOT EXISTS child (card_id INT NOT NULL PRIMARY KEY, card_num VARCHAR(255), client_id INT NOT NULL, FOREIGN KEY (client_id) REFERENCES father(id) ON UPDATE RESTRICT ON DELETE RESTRICT)")

    def INSERT_father(cr):

        cr.execute("INSERT INTO father (id, username, email) VALUES (%s, %s, %s)", (1, "john_doe", "john.doe@example.com"))

        cr.execute("INSERT INTO father (id, username, email) VALUES (%s, %s, %s)", (2, "ahmed", "ahmed@example.com"))

    def INSERT_child(cr):

        cr.execute("INSERT INTO child (card_id, card_num, client_id) VALUES (%s, %s, %s)", (1, "123456789", 1))

        cr.execute("INSERT INTO child (card_id, card_num, client_id) VALUES (%s, %s, %s)", (3, "123456782", 2))

        cr.execute("INSERT INTO child (card_id, card_num, client_id) VALUES (%s, %s, %s)", (5, "423456752", None))


    def CHANGE_child(cr):

        # cr.execute("ALTER TABLE child CHANGE card_num card_num VARCHAR(255) NOT NULL UNIQUE")

        cr.execute("ALTER TABLE child CHANGE client_id client_id INT NULL UNIQUE")



    def CHANGE(cr):

        # cr.execute("ALTER TABLE ordere CHANGE client_id client_id INT NULL")

        # cr.execute("ALTER TABLE child DROP FOREIGN KEY child_ibfk_1")

        # cr.execute("ALTER TABLE child DROP INDEX child_ibfk_1")

        cr.execute("ALTER TABLE child ADD CONSTRAINT child_ibfk_1 FOREIGN KEY (client_id) REFERENCES father(id) ON UPDATE CASCADE ON DELETE CASCADE")

    def SHOW(cr):

        cr.execute("SHOW CREATE TABLE child")

        for row in cr:

            print(row)
    
    def delete(cr):

        cr.execute("DELETE FROM child WHERE card_id = 4")

        cr.execute("DELETE FROM child WHERE card_id = 5")


    # SHOW(cr)

    # CHANGE(cr)

    # INSERT_father(cr)

    INSERT_child(cr)

    # delete(cr)

    # CHANGE_child(cr)



    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:
    
    if db:
        
        db.close()