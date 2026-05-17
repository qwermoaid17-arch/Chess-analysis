import pymysql as sql

try:

    db = sql.connect(
        host = "localhost",
        user = "root",
        password = "",
        charset='utf8mb4'
    )

    cr = db.cursor()

    cr.execute("CREATE DATABASE IF NOT EXISTS project_foreign")

    cr.execute("USE project_foreign")

    cr.execute("CREATE TABLE IF NOT EXISTS teacher (id INT PRIMARY KEY, name VARCHAR(100), specialty VARCHAR(100) NOT NULL)")

    cr.execute("CREATE TABLE IF NOT EXISTS instructor_profiles (profile_id INT PRIMARY KEY, biography TEXT, phone_number VARCHAR(20), instructor_id INT NOT NULL, FOREIGN KEY (instructor_id) REFERENCES teacher(id) ON UPDATE CASCADE ON DELETE CASCADE)")

    cr.execute("CREATE TABLE IF NOT EXISTS courses (course_id INT PRIMARY KEY, course_title VARCHAR(100), instructor_id INT NOT NULL, FOREIGN KEY (instructor_id) REFERENCES teacher(id) ON UPDATE CASCADE ON DELETE RESTRICT)")

    cr.execute("CREATE TABLE IF NOT EXISTS students (student_id INT PRIMARY KEY, name VARCHAR(100))")

    cr.execute("CREATE TABLE IF NOT EXISTS enrollments (student INT NOT NULL, course INT NOT NULL, PRIMARY KEY(student, course), FOREIGN KEY (student) REFERENCES students(student_id) ON UPDATE CASCADE ON DELETE CASCADE, FOREIGN KEY (course) REFERENCES courses(course_id) ON UPDATE CASCADE ON DELETE CASCADE)")


    def INSERT_teacher(cr):

        cr.execute("INSERT INTO teacher (id, name, specialty) VALUES (%s, %s, %s)", (1, "John Doe", "Mathematics"))

        cr.execute("INSERT INTO teacher (id, name, specialty) VALUES (%s, %s, %s)", (2, "Jane Smith", "Physics"))

    def INSERT_instructor_profiles(cr):

        cr.execute("INSERT INTO instructor_profiles (profile_id, biography, phone_number, instructor_id) VALUES (%s, %s, %s, %s)", (1, "John Doe is an experienced mathematics instructor with a passion for teaching.", "123-456-7890", 1))

        cr.execute("INSERT INTO instructor_profiles (profile_id, biography, phone_number, instructor_id) VALUES (%s, %s, %s, %s)", (2, "Jane Smith is a dedicated physics instructor with a strong background in research.", "987-654-3210", 2))
    
    def INSERT_courses(cr):

        cr.execute("INSERT INTO courses (course_id, course_title, instructor_id) VALUES (%s, %s, %s)", (1, "Calculus 101", 1))

        cr.execute("INSERT INTO courses (course_id, course_title, instructor_id) VALUES (%s, %s, %s)", (2, "Physics 101", 2))

    def INSERT_students(cr):

        cr.execute("INSERT INTO students (student_id, name) VALUES (%s, %s)", (1, "Alice"))

        cr.execute("INSERT INTO students (student_id, name) VALUES (%s, %s)", (2, "Bob"))

    def INSERT_enrollments(cr):

        cr.execute("INSERT INTO enrollments (student, course) VALUES (%s, %s)", (1, 1))

        cr.execute("INSERT INTO enrollments (student, course) VALUES (%s, %s)", (2, 2))
    
    def delete_teacher(cr):

        cr.execute("DELETE FROM teacher WHERE id = %s", (1,))

    def CHANGE(cr):

        cr.execute("ALTER TABLE instructor_profiles CHANGE COLUMN instructor_id instructor_id INT NOT NULL UNIQUE")



    
    # Calling functions

    INSERT_teacher(cr)

    INSERT_instructor_profiles(cr)

    INSERT_courses(cr)

    INSERT_students(cr)

    INSERT_enrollments(cr)

    # CHANGE(cr)

    # delete_teacher(cr)

    db.commit()

except sql.err.IntegrityError:

    print("This teacher cannot be deleted; their role is not yet complete.")

except sql.Error as er:

    print("Error ", er)

finally:

    if db:
        db.close()