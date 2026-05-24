import pymysql as sql 

try:

    db = sql.connect(
        host = "localhost",
        user = "root",
        password = "",
        charset='utf8mb4'
    )


    cr = db.cursor()

    cr.execute("USE tests")

    def INSERT(cr):

        # cr.execute("INSERT INTO users (text) VALUES (%s)", ("  moayed  ",))

        cr.execute("INSERT INTO users (text) VALUES (%s)", ("www.elzero.org",))
    
    def DELETE(cr):

        cr.execute("DELETE FROM users WHERE id BETWEEN  20 AND 25")

    def SELECT_TRIM(cr):

        # cr.execute("SELECT text, TRIM(text) as trimmed FROM users")

        # cr.execute("SELECT text, TRIM(LEADING FROM text) as trimmed FROM users")

        # cr.execute("SELECT text, TRIM(TRAILING FROM text) as trimmed FROM users")

        # This is what happens when you leave it with nothing

        # cr.execute("SELECT text, TRIM(BOTH FROM text) as trimmed FROM users")

        # cr.execute("SELECT text, TRIM(BOTH FROM text) as trimmed, CHAR_LENGTH(text) as length_text, CHAR_LENGTH(TRIM(BOTH FROM text)) as length_trimmed FROM users")

        # cr.execute("SELECT text, TRIM(LEADING FROM text) as trimmed, CHAR_LENGTH(text) as length_text, CHAR_LENGTH(TRIM(LEADING FROM text)) as length_trimmed FROM users")

        # cr.execute("SELECT text, TRIM(LEADING '@' FROM text) as trimmed, CHAR_LENGTH(text) as length_text, CHAR_LENGTH(TRIM(LEADING '@' FROM text)) as length_trimmed FROM users")

        # cr.execute("SELECT text, TRIM(TRAILING '@' FROM text) as trimmed, CHAR_LENGTH(text) as length_text, CHAR_LENGTH(TRIM(TRAILING '@' FROM text)) as length_trimmed FROM users")

        # cr.execute("SELECT text, TRIM('@' FROM text) as trimmed, CHAR_LENGTH(text) as length_text, CHAR_LENGTH(TRIM('@' FROM text)) as length_trimmed FROM users")

        # Anuther way

        # cr.execute("SELECT text, TRIM(BOTH '@' FROM text) as trimmed, CHAR_LENGTH(text) as length_text, CHAR_LENGTH(TRIM(BOTH '@' FROM text)) as length_trimmed FROM users")

        # Anuther way

        # cr.execute("SELECT text, RTRIM(text) as trimmed, CHAR_LENGTH(text) as length_text, CHAR_LENGTH(RTRIM(text)) as length_trimmed FROM users")

        cr.execute("SELECT text, LTRIM(text) as trimmed, CHAR_LENGTH(text) as length_text, CHAR_LENGTH(LTRIM(text)) as length_trimmed FROM users")

    

        result = cr.fetchall()

        for row in result:

            print(f"Text: {row[0]}, Trimmed: {row[1]}, Length_text: {row[2]}, Length_trimmed: {row[3]}")

    def UPDATE(cr):

        # cr.execute("UPDATE users SET text = %s" , ("  moayed  ",))


        cr.execute("UPDATE users SET text = %s WHERE id = %s" , ("www.elzero.org", 27))    

    def TRIM_UPDATE(cr):

        cr.execute("UPDATE users SET text = TRIM(LEADING 'www.' FROM text) WHERE id = %s",  (27,))

        cr.execute("UPDATE users SET text = TRIM(TRAILING '.org' FROM text) WHERE id = %s",  (27,))


    
    def SHOW(cr):

        cr.execute("SELECT text FROM users")

        result = cr.fetchall()

        for row in result:

            print(f"Text: {row[0]}")
    

    # Calling functions

    # INSERT(cr)

    # DELETE(cr)

    UPDATE(cr)

    TRIM_UPDATE(cr)

    # SELECT_TRIM(cr)

    SHOW(cr)

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:
        db.close()