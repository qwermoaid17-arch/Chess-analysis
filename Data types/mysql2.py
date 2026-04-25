import pymysql as sql

try:

    db = sql.connect(
        host = "localhost",
        user="root",
        password="",
        charset='utf8mb4',
        database="tests"
    )

    cr = db.cursor()

    cr.execute("CREATE TABLE IF NOT EXISTS items (id INT)")

    # cr.execute("ALTER TABLE items ADD  COLUMN ic TINYINT")

    # cr.execute("ALTER TABLE items ADD  COLUMN ia SMALLINT")

    # cr.execute("ALTER TABLE items ADD  COLUMN ib MEDIUMINT")

    # cr.execute("ALTER TABLE items ADD COLUMN ih BOOL")

    


    # cr.execute("INSERT INTO items (ia) VALUES (%s)",(32777,))

    # cr.execute("USE tests")

    # cr.execute("INSERT INTO items (name) VALUES (%s)",("منتج6",))


    cr.execute("INSERT INTO items (ie) VALUES (%s)",(1,))

    cr.execute("INSERT INTO items (bd) VALUES (%s)",(14,))


    cr.execute("INSERT INTO items (bd) VALUES (%s)",(12,))

    for i in range(10):

        cr.execute("INSERT INTO items (bd) VALUES (%s)",(10,))

    db.commit()

except sql.Error as er:

    print("Error: ",er)