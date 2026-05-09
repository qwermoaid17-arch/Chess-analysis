import pymysql as sql

try:

    db = sql.connect(
        host = "localhost",
        user = "root",
        password = "",
        charset='utf8mb4'
    )

    cr = db.cursor()

    cr.execute("USE moayed")

    # cr.execute("CREATE TABLE IF NOT EXISTS students "
    # "(id INT AUTO_INCREMENT PRIMARY KEY, " \
    # " name VARCHAR(255), " \
    # "email VARCHAR(255))")

    # cr.execute("INSERT INTO students(maoyed, id, name, email, password, username, ahmed, test) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", ("moayed", 1, "John Doe", "john.doe@example.com", "password123", "johndoe", "ahmed", "test"))

    # cr.execute("ALTER TABLE students ADD  UNIQUE(username)")

    # cr.execute("ALTER TABLE students ADD COLUMN test VARCHAR(255) NOT NULL UNIQUE")

    # cr.execute("ALTER TABLE students DROP INDEX username")

    db.commit()

    db.close()

except sql.Error as er:

    print("Error ", er)