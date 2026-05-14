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

    # cr.execute("DROP TABLE IF EXISTS comments")

    cr.execute("CREATE TABLE IF NOT EXISTS comments (c_id INT NOT NULL PRIMARY KEY, comment VARCHAR(255), client_id INT NOT NULL, FOREIGN KEY (client_id) REFERENCES client(id) ON UPDATE CASCADE ON DELETE CASCADE)")

    def INSERT_client(cr):

        cr.execute("INSERT INTO client (id, username, email) VALUES (%s, %s, %s)", (1, "john_doe", "john.doe@example.com"))

        # cr.execute("INSERT INTO client (id, username, email) VALUES (%s, %s, %s)", (2, "ahmed", "ahmed@example.com"))

        # cr.execute("INSERT INTO client (id, username, email) VALUES (%s, %s, %s)", (3, "alaa", "alaa@example.com"))
    
    def INSERT_orders(cr):

        cr.execute("INSERT INTO orders (order_id, price, client_id) VALUES (%s, %s, %s)", (1, 100.00, 1))

        cr.execute("INSERT INTO orders (order_id, price, client_id) VALUES (%s, %s, %s)", (2, 200.00, 1))

        cr.execute("INSERT INTO orders (order_id, price, client_id) VALUES (%s, %s, %s)", (3, 50.00, 1))

    def INSERT_comments(cr):

        cr.execute("INSERT INTO comments (c_id, comment, client_id) VALUES (%s, %s, %s)", (1, "This is a comment", 1))

        cr.execute("INSERT INTO comments (c_id, comment, client_id) VALUES (%s, %s, %s)", (2, "This is another comment", 1))

        cr.execute("INSERT INTO comments (c_id, comment, client_id) VALUES (%s, %s, %s)", (3, "This is yet another comment", 1))

    def CHANGE(cr):

        cr.execute("ALTER TABLE orders DROP FOREIGN KEY orders_ibfk_1")

        # cr.execute("ALTER TABLE orders DROP INDEX orders_ibfk_1")

        cr.execute("ALTER TABLE orders ADD CONSTRAINT orders_ibfk_1 FOREIGN KEY (client_id) REFERENCES client(id) ON UPDATE CASCADE ON DELETE CASCADE")

        cr.execute("ALTER TABLE comments DROP FOREIGN KEY comments_ibfk_1")

        cr.execute("ALTER TABLE comments ADD CONSTRAINT comments_ibfk_1 FOREIGN KEY (client_id) REFERENCES client(id) ON UPDATE CASCADE ON DELETE CASCADE")

        # cr.execute("ALTER TABLE ordere DROP FOREIGN KEY ordere")

        # cr.execute("ALTER TABLE ordere ADD CONSTRAINT ordere FOREIGN KEY (client_id) REFERENCES client(id) ON UPDATE CASCADE ON DELETE CASCADE")

    def CHANGE_orders(cr):

        cr.execute("ALTER TABLE orders DROP INDEX client_id")

    def delete(cr):

        # cr.execute ("ALTER TABLE comments DROP FOREIGN KEY comments_ibfk_1")

        # cr.execute("ALTER TABLE comments DROP INDEX comments_ibfk_1")

        cr.execute("DELETE FROM client WHERE id = %s", (1,))

    def SHOW(cr):

        # cr.execute("SHOW CREATE TABLE client")

        # cr.execute("SHOW CREATE TABLE comments")

        # cr.execute("SHOW CREATE TABLE orders")

        for row in cr:

            print(row)
    def show_client_orders(cr):

        cr.execute("SELECT TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME FROM information_schema.KEY_COLUMN_USAGE WHERE REFERENCED_TABLE_SCHEMA = 'constraints'")


        # cr.execute("SELECT TABLE_NAME, CONSTRAINT_NAME, DELETE_RULE, UPDATE_RULE, REFERENCED_TABLE_NAME FROM information_schema.REFERENTIAL_CONSTRAINTS WHERE CONSTRAINT_SCHEMA = 'constraints'")

        for row in cr.fetchall():

            print("-", row)
        
    def SHOW_orders(cr):

        cr.execute("SHOW CREATE TABLE orders")

        for row in cr:

            print(row)


    # SHOW(cr)

    # INSERT_client(cr)

    # INSERT_orders(cr)

    # INSERT_comments(cr)

    # CHANGE(cr)

    # CHANGE_orders(cr)

    delete(cr)

    # show_client_orders(cr)

    # SHOW_orders(cr)

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:
    
    if db:
        
        db.close()