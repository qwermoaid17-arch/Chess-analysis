import pymysql as sql

try:

    db = sql.connect(
        host = "localhost",
        user="root",
        passwd="",
        charset='utf8mb4'
    )

    cr = db.cursor()

    cr.execute("CREATE DATABASE IF NOT EXISTS store_db ")

    cr.execute("USE store_db")

    cr.execute("DROP TABLE IF EXISTS draft_products, final_products")

    cr.execute("CREATE TABLE IF NOT EXISTS draft_products (id INT AUTO_INCREMENT PRIMARY KEY, product_name VARCHAR(255))")

    cr.execute("RENAME TABLE draft_products TO final_products")

    cr.execute("ALTER TABLE final_products ENGINE = MyISAM")

    cr.execute("SHOW TABLE STATUS FROM store_db")

    for i in cr:

        print(i)

    db.commit()
    db.close()

except sql.Error as er:
    
    print("Error ", er)