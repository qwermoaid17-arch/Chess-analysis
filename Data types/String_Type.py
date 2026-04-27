import pymysql as sql

try:

    db = sql.connect(
        host = "localhost",
        user = "root",
        password = "",
        charset='utf8mb4'
    )

    with open(r"C:\Users\qwerm\Pictures\Camera Roll\WIN_20260425_19_36_53_Pro.jpg", "rb") as f:
        img = f.read()

    cr = db.cursor()

    cr.execute("CREATE DATABASE IF NOT EXISTS String_Type")

    cr.execute("USE String_Type")

    cr.execute("CREATE TABLE IF NOT EXISTS tbl (id INT AUTO_INCREMENT PRIMARY KEY, string CHAR(1), name VARCHAR(100))")

    # cr.execute("ALTER TABLE tbl ADD COLUMN string2 TEXT")

    # cr.execute("ALTER TABLE tbl ADD COLUMN string3 BLOB")

    # cr.execute("ALTER TABLE tbl ADD COLUMN string4 ENUM('python', 'java', 'c++', 'html' )")

    cr.execute("INSERT INTO tbl (string4, string5, string2, string3,) VALUES (%s,%s,%s,%s)", ("python","google,Brave", "This is a text", img))

    # cr.execute("ALTER TABLE tbl ADD COLUMN string5 SET('google', 'Brave', 'Firefox', 'Edge')")

    # cr.execute("INSERT INTO tbl (string5) VALUES (%s)", ("google,Brave",))


    # cr.execute("INSERT INTO tbl (string2, string3) VALUES (%s, %s)", ("This is a text", img))

    for i in range(10):

        cr.execute("INSERT INTO tbl (String, name) VALUES (%s, %s)", (i, i))
    
    db.commit()

    db.close()

except sql.Error as er:
    print("Error ", er)    