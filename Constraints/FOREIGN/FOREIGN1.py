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

    cr.execute("CREATE TABLE IF NOT EXISTS clients (id INT NOT NULL PRIMARY KEY, username VARCHAR(100) UNIQUE, email VARCHAR(255) NOT NULL UNIQUE)")

    cr.execute("CREATE TABLE IF NOT EXISTS orders (order_id INT NOT NULL PRIMARY KEY, price DECIMAL(10, 2), client_id INT NOT NULL, FOREIGN KEY (client_id) REFERENCES clients(id))")

    cr.execute("INSERT INTO clients (id, username, email) VALUES (%s, %s, %s)", (1, "john_doe", "john.doe@example.com"))

    cr.execute("INSERT INTO orders (order_id, price, client_id) VALUES (%s, %s, %s)", (1, 100.00, 1))

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:
        
        db.close()