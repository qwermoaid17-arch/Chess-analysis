import pymysql as sql

try:

    db = sql.connect(
        host = "localhost",
        user = "root",
        password = "",
        charset='utf8mb4'
    )

    cr = db.cursor()

    cr.execute("CREATE DATABASE IF NOT EXISTS project_str")

    cr.execute("USE project_str")

    cr.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, raw_name VARCHAR(100) NOT NULL, email VARCHAR(255) NOT NULL UNIQUE, old_phone VARCHAR(20), accont_type VARCHAR(100), old_card VARCHAR(20))")

    def INSERT(cr):

        cr.execute("INSERT INTO users (raw_name, email, old_phone, accont_type, old_card) VALUES (%s, %s, %s, %s, %s)", ("  moayed&  ", "aHOluj@outlook.sa", "0020101234567", "vip", "7414"))

        cr.execute("INSERT INTO users (raw_name, email, old_phone, accont_type, old_card) VALUES (%s, %s, %s, %s, %s)", ("  ahmed*&  ", "HOkoj@outlook.sa", "0021891765432", "plus", "741489"))

        cr.execute("INSERT INTO users (raw_name, email, old_phone, accont_type, old_card) VALUES (%s, %s, %s, %s, %s)", ("  ^lalala&  ", "QWEasdh@gmail.com", "0096650987654", "pro", "5462"))

    def SELECT_TRIM(cr):

        cr.execute("SELECT TRIM( ' ' FROM REGEXP_REPLACE(raw_name, '[&,*,^]', ' ') ) as trimmed FROM users")

        result = cr.fetchall()

        for row in result:

            print(row[0])

    def SELECT_MID(cr):

        cr.execute("SELECT LEFT(old_phone, 5), RIGHT(old_phone, 7), MID(old_phone, 6, 2) FROM users")

        result = cr.fetchall()

        for row in result:

            print(f"LEFT : {row[0]} RIGHT : {row[1]}  MID : {row[2]}")
    
    def SELECT_VALIDATION(cr):

        cr.execute("SELECT UCASE(email), LCASE(email), LENGTH(email), CHAR_LENGTH(email) FROM users")

        result = cr.fetchall()

        for row in result:

            print(f"UPPER: {row[0]}, LOWER: {row[1]}, LENGTH: {row[2]}, CHAR_LENGTH: {row[3]}")

    def SELECT_UPGRADE(cr):

        cr.execute("SELECT CONCAT_WS(' - ' , raw_name, REPLACE(email, 'outlook.sa', 'gmail.com'), accont_type) FROM users")

        result = cr.fetchall()

        for row in result:

            print(row[0])

    def SELECT_SECURITY(cr):

        cr.execute("SELECT REVERSE(LPAD(old_card, 10, '0')), REVERSE(RPAD(old_card, 10, '*'))  FROM users")

        # cr.execute("SELECT REVERSE(RPAD(old_card, 10, '*')) FROM users")

        result = cr.fetchall()

        for row in result:

            print(f"Reversed: {row[0]}, Padded: {row[1]}")

    # Calling the function:

    # INSERT(cr)

    # SELECT_TRIM(cr)

    # SELECT_MID(cr)

    # SELECT_VALIDATION(cr)

    # SELECT_UPGRADE(cr)

    SELECT_SECURITY(cr)

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:
        db.close()