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

    cr.execute("CREATE TABLE IF NOT EXISTS client (id INT NOT NULL PRIMARY KEY, username VARCHAR(100) UNIQUE, email VARCHAR(255) NOT NULL UNIQUE)")

    cr.execute("CREATE TABLE IF NOT EXISTS ordere (order_id INT NOT NULL PRIMARY KEY, price DECIMAL(10, 2), client_id INT NOT NULL)")

    def ALTER_FOREIGN_KEY(cr):

        cr.execute("ALTER TABLE ordere ADD CONSTRAINT ordrere FOREIGN KEY (client_id) REFERENCES client(id) ON UPDATE CASCADE ON DELETE CASCADE")

    def INSERT_client(cr):

        cr.execute("INSERT INTO client (id, username, email) VALUES (%s, %s, %s)", (1, "maoyed", "john.doe@example.com"))

        cr.execute("INSERT INTO client (id, username, email) VALUES (%s, %s, %s)", (2, "ahmed", "ahmed@example.com"))

        cr.execute("INSERT INTO client (id, username, email) VALUES (%s, %s, %s)", (3, "alaa", "alaa@example.com"))

        cr.execute("INSERT INTO client (id, username, email) VALUES (%s, %s, %s)", (100, "mohamed", "mohamed@example.com"))

    def INSERT_ordere(cr):

        cr.execute("INSERT INTO ordere (order_id, price, client_id) VALUES (%s, %s, %s)", (1, 100.00, 1))

        cr.execute("INSERT INTO ordere (order_id, price, client_id) VALUES (%s, %s, %s)", (2, 200.00, 1))

        cr.execute("INSERT INTO ordere (order_id, price, client_id) VALUES (%s, %s, %s)", (3, 50.00, 1))

        cr.execute("INSERT INTO ordere (order_id, price, client_id) VALUES (%s, %s, %s)", (4, 150.00, 2))

        cr.execute("INSERT INTO ordere (order_id, price, client_id) VALUES (%s, %s, %s)", (5, 75.00, 2))
    
    def show_client_orders_1(cr):

        cr.execute("SELECT * FROM ordere join client on client.id = ordere.client_id where client.id = 1")

        for row in cr.fetchall():

            print("-", row)

    def show_client_orders_2(cr):

        cr.execute("SELECT * FROM ordere join client on client.id = ordere.client_id where client.id = 2")

        for row in cr.fetchall():

            print("-", row)

    def UPDATE_moayed(cr):

        cr.execute("UPDATE client SET id = %s WHERE username = %s", (50, "maoyed"))

    def DELETE_moayed(cr):

        cr.execute("DELETE FROM client WHERE username = %s", ("maoyed",))

    def UPDATE_ahmed(cr):

        cr.execute("UPDATE client SET id = %s WHERE username = %s", (200, "ahmed"))

    def DELETE_ahmed(cr):

        cr.execute("DELETE FROM client WHERE username = %s", ("ahmed",))

    # Calling functions

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:
        
        db.close()