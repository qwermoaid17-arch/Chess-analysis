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

    cr.execute("CREATE TABLE IF NOT EXISTS user (id INT NOT NULL PRIMARY KEY, username VARCHAR(100) UNIQUE, email VARCHAR(255) NOT NULL UNIQUE)")

    def INSERT_user(cr):

        cr.execute("INSERT INTO user (id, username, email) VALUES (%s, %s, %s)", (1, "moayed", "john.doe@example.com"))

        cr.execute("INSERT INTO user (id, username, email) VALUES (%s, %s, %s)", (2, "ahmed", "ahmed@example.com"))

        cr.execute("INSERT INTO user (id, username, email) VALUES (%s, %s, %s)", (3, "alaa", "alaa@example.com"))



    cr.execute("CREATE TABLE IF NOT EXISTS shops (shop_id INT NOT NULL PRIMARY KEY, name VARCHAR(255))")

    def INSERT_shops(cr):

        cr.execute("INSERT INTO shops (shop_id, name) VALUES (%s, %s)", (1, "Shop_maoyed"))

        cr.execute("INSERT INTO shops (shop_id, name) VALUES (%s, %s)", (2, "Shop ahmed"))

        cr.execute("INSERT INTO shops (shop_id, name) VALUES (%s, %s)", (3, "Shop alaa"))

    cr.execute("CREATE TABLE IF NOT EXISTS shope_member (user INT NOT NULL, shope INT NOT NULL, PRIMARY KEY(user, shope), CONSTRAINT cons_user FOREIGN KEY (user) REFERENCES user(id) ON UPDATE CASCADE ON DELETE CASCADE, CONSTRAINT cons_shope FOREIGN KEY (shope) REFERENCES shops(shop_id) ON UPDATE CASCADE ON DELETE CASCADE )")

    def supsecripe(cr):

        # cr.execute("INSERT INTO shope_member (user, shope) VALUES (%s, %s)", (1, 1))

        # cr.execute("INSERT INTO shope_member (user, shope) VALUES (%s, %s)", (1, 2))

        # cr.execute("INSERT INTO shope_member (user, shope) VALUES (%s, %s)", (1, 3))

        # cr.execute("INSERT INTO shope_member (user, shope) VALUES (%s, %s)", (2, 1))

        cr.execute("INSERT INTO shope_member (user, shope) VALUES (%s, %s)", (3, 1))

    def UPDATE(cr):

        cr.execute("UPDATE user SET id = %s WHERE id = %s", (10, 1))

        cr.execute("UPDATE shops SET shop_id = %s WHERE shop_id = %s", (20, 1))    

    def search(cr):

        # cr.execute("SELECT * FROM user join shope_member ON user.id = shope_member.user WHERE shope_member.shope = 1")

        cr.execute("SELECT * FROM shops join shope_member ON shops.shop_id = shope_member.shope WHERE shope_member.user = 2")

        for row in cr.fetchall():

            print("-", row)


    # Calling functions

    # INSERT_user(cr)

    # INSERT_shops(cr)

    # supsecripe(cr)

    search(cr)

    UPDATE(cr)

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:
        db.close()