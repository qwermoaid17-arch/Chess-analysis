import pymysql as sql

try:

    db = sql.connect(
        host = "localhost",
        user="root",
        passwd="",
        charset='utf8mb4'
    )

    cr = db.cursor()

    cr.execute("CREATE DATABASE IF NOT EXISTS company_db")
    cr.execute("USE company_db")

    cr.execute("CREATE TABLE IF NOT EXISTS employees (id INT AUTO_INCREMENT PRIMARY KEY, emp_name VARCHAR(50))")

    cr.execute("ALTER TABLE employees ADD COLUMN IF NOT EXISTS email VARCHAR(255) AFTER emp_name")

    cr.execute("ALTER TABLE employees ADD COLUMN IF NOT EXISTS job_code VARCHAR(20) FIRST")

    cr.execute("ALTER TABLE employees CHANGE COLUMN IF EXISTS emp_name full_name VARCHAR(255)")

    cr.execute("ALTER TABLE employees ADD COLUMN IF NOT EXISTS old_salary INT")

    cr.execute("ALTER TABLE employees DROP COLUMN IF EXISTS old_salary")

    cr.execute("SHOW COLUMNS FROM employees")

    for i in cr:
        print(i)

    db.commit()
    db.close()

except sql.Error as er:

    print("Error ", er)