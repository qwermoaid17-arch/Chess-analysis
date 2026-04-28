import pymysql as sql

article="""Running is one of the most accessible and effective forms of exercise, requiring little more than a pair of shoes and determination. This review highlights the benefits of regular running for both physical health and athletic performance.

From a health perspective, running improves cardiovascular endurance, strengthens muscles, and helps maintain a healthy weight. Studies show that consistent running reduces the risk of heart disease, diabetes, and high blood pressure. It also boosts mental well‑being by releasing endorphins, often referred to as the runner’s high.

In terms of sports performance, running builds stamina and resilience. Athletes in various disciplines, from football to martial arts, use running as a foundation for conditioning. It enhances agility, speed, and recovery, making it a versatile training tool.

However, discipline and moderation are essential. Overtraining can lead to injuries such as shin splints or knee pain. A balanced routine that includes rest, stretching, and proper nutrition ensures that running remains sustainable and beneficial.

In conclusion, regular running is more than just a workout; it is a lifestyle choice that promotes long‑term health and supports athletic excellence. With perseverance and discipline, anyone can harness its full potential."""




try:

    db = sql.connect(
        host = "localhost",
        user="root",
        passwd="",
        charset='utf8mb4'
    )




    cr = db.cursor()

    cr.execute("CREATE DATABASE IF NOT EXISTS cms_db ")
    cr.execute("USE cms_db")

    cr.execute("CREATE TABLE IF NOT EXISTS posts (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(155), content TEXT, catogory ENUM('Tech', 'Health', 'Sports'), tags SET('news', 'review', 'tutorial', 'update'), anuthor_code CHAR(5))")

    cr.execute("INSERT INTO posts (title, content,catogory, tags, anuthor_code) VALUES (%s, %s, %s, %s, %s),(%s, %s, %s, %s, %s)",
                ("Review: The Impact of Regular Running on Health and Performance",article, "sports", "news,review", "A1234",
                 "Tutorial: How to Start Running for Beginners", "This tutorial provides a step-by-step guide for beginners looking to start running. It covers essential tips on choosing the right shoes, creating a training plan, and staying motivated. Whether you're aiming to run your first 5K or simply want to improve your fitness, this guide will help you get started on the right foot.", "Tech", "tutorial,update", "B5678"))
    

    
    db.commit()
    db.close()

except sql.Error as er:

    print("Error ", er)