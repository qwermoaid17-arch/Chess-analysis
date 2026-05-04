import pymysql as sql

try:

    db = sql.connect(
        host = "localhost",
        user = "root",
        password = "",
        charset='utf8mb4'
    )

    cr = db.cursor()

    cr.execute("CREATE DATABASE IF NOT EXISTS yyy")
    cr.execute("USE yyy")

    cr.execute("CREATE TABLE IF NOT EXISTS departments (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100))")

    cr.execute("CREATE TABLE IF NOT EXISTS employees (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), salary DECIMAL(10, 2), department_id INT, FOREIGN KEY (department_id) REFERENCES departments(id))")

    cr.execute("INSERT INTO departments (name) VALUES (%s)", ("HR",))

    cr.execute("INSERT INTO employees (name, salary, department_id) VALUES (%s, %s, %s)", ("Alice", 50000.00, 11))

    db.commit()

    db.close()



except sql.Error as er:

    print("Error ", er)