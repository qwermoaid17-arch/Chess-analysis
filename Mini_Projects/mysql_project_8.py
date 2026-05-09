import pymysql as sql

try:
    db = sql.connect(
        host = "localhost",
        user = "root",
        password = "",
        charset='utf8mb4'
    )

    cr = db.cursor()

    cr.execute("CREATE DATABASE IF NOT EXISTS company_dd")

    cr.execute("USE company_dd")

    cr.execute("CREATE TABLE IF NOT EXISTS employees (emp_id INT AUTO_INCREMENT PRIMARY KEY, national_id VARCHAR(20) NOT NULL UNIQUE, name VARCHAR(255) NOT NULL, department_code VARCHAR(255) NOT NULL)")

    # cr.execute("INSERT INTO employees (national_id, name, department_code) VALUES (%s, %s, %s)", ("123456789023", "John Doe", "HR"))

    # cr.execute("INSERT INTO employees (national_id, name, department_code) VALUES (%s, %s, %s)", ("543210987654", "moayed", "eo945"))

    #error

    cr.execute("INSERT INTO employees (national_id, name, department_code) VALUES (%s, %s, %s)", ("123456789023", "John Doe", "HR"))


    db.commit()

except sql.IntegrityError:

    print("This national ID number already exists. Please use a unique national ID.")

except sql.Error as er:

    print("Error ", er)

finally:

    db.close()