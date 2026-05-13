import pymysql as sql

try:

    db = sql.connect(
        host = "localhost",
        user = "root",
        password = "",
        charset='utf8mb4'
    )

    cr = db.cursor()

    cr.execute("USE Constraints")

    cr.execute("CREATE TABLE IF NOT EXISTS client (id INT NOT NULL PRIMARY KEY, username VARCHAR(100) UNIQUE, email VARCHAR(255) NOT NULL UNIQUE)")

    cr.execute("CREATE TABLE IF NOT EXISTS ordere (order_id INT NOT NULL PRIMARY KEY, price DECIMAL(10, 2), client_id INT NOT NULL, FOREIGN KEY (client_id) REFERENCES client(id) ON UPDATE CASCADE ON DELETE CASCADE)")

    def INSERT_client(cr):

        cr.execute("INSERT INTO client (id, username, email) VALUES (%s, %s, %s)", (2, "john_doe", "john.doe@example.com"))

        # cr.execute("INSERT INTO client (id, username, email) VALUES (%s, %s, %s)", (100, "mohamed", "mohamed@example.com"))

        cr.execute("INSERT INTO client (id, username, email) VALUES (%s, %s, %s)", (1, "ahmed", "ahmed@example.com"))

    def INSERT_ordere(cr):

        cr.execute("INSERT INTO ordere (order_id, price, client_id) VALUES (%s, %s, %s)", (1, 100.00, 2))

        cr.execute("INSERT INTO ordere (order_id, price, client_id) VALUES (%s, %s, %s)", (2, 200.00, 2))
    
    def delete(cr):

        # cr.execute("DELETE FROM ordere WHERE order_id = 2")

        # cr.execute("DELETE FROM ordere WHERE order_id = 1")


        # cr.execute("DELETE FROM client WHERE id = %s", (2,))

        cr.execute("DELETE FROM client WHERE id = %s", (1,))

    
    def update(cr):

        # cr.execute("UPDATE client SET id = 20 WHERE id = 1")

        # cr.execute("UPDATE client SET id = %s WHERE id = %s", (2, 100))

        cr.execute("UPDATE ordere SET client_id = %s WHERE order_id = %s", (1, 2))

        # cr.execute("UPDATE ordere SET client_id = %s WHERE order_id = %s", (1, 1))


    
    def CHANGE(cr):

        # cr.execute("ALTER TABLE ordere CHANGE client_id client_id INT NULL")

        # cr.execute("ALTER TABLE ordere DROP FOREIGN KEY ordere")

        # cr.execute("ALTER TABLE ordere DROP INDEX ordere")

        # cr.execute("ALTER TABLE ordere ADD CONSTRAINT ordere FOREIGN KEY (client_id) REFERENCES client(id) ON UPDATE SET NULL ON DELETE SET NULL")

        cr.execute("ALTER TABLE ordere ADD CONSTRAINT ordere FOREIGN KEY (client_id) REFERENCES client(id) ON UPDATE RESTRICT ON DELETE RESTRICT")

    def SHOW(cr):

        cr.execute("SHOW CREATE TABLE ordere")

        for row in cr:

            print(row)

    # INSERT_client(cr)

    # INSERT_ordere(cr)

    # update(cr)

    delete(cr)

    # SHOW(cr)

    # CHANGE(cr)

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:
        db.close()