import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

cur.execute("INSERT INTO student_submission (submission_id, course_work_id, course_id, student_id, _status, assigned_points, max_points) VALUES (?,?,?,?,?,?,?)",
             ('1','11','342','34','NEW','2.0','2.8')
             )

cur.execute("INSERT INTO student_submission (submission_id, course_work_id, course_id, student_id, _status, assigned_points, max_points) VALUES (?,?,?,?,?,?,?)",
             ('2','31','322','84','TURNED_IN','1.6','1.3')
             )

cur.execute("INSERT INTO student_submission (submission_id, course_work_id, course_id, student_id, _status, assigned_points, max_points) VALUES (?,?,?,?,?,?,?)",
             ('3','41','362','54','NEW','2.1','1.8')
            )

cur.execute("INSERT INTO student_submission (submission_id, course_work_id, course_id, student_id, _status, assigned_points, max_points) VALUES (?,?,?,?,?,?,?)",
             ('4','72','262','54','TURNED_IN','3.1','1.5')
            )

cur.execute("INSERT INTO student_submission (submission_id, course_work_id, course_id, student_id, _status, assigned_points, max_points) VALUES (?,?,?,?,?,?,?)",
             ('5','72','161','54','TURNED_IN','3','1.1')
            )

cur.execute("INSERT INTO roster (student_id, course_id) VALUES (?,?)",('54','362'))
cur.execute("INSERT INTO roster (student_id, course_id) VALUES (?,?)",('34','346'))
cur.execute("INSERT INTO roster (student_id, course_id) VALUES (?,?)",('84','322'))

cur.execute("INSERT INTO student (student_id, school, grade_level) VALUES (?,?,?)",('54','333','2'))
cur.execute("INSERT INTO student (student_id, school, grade_level) VALUES (?,?,?)",('34','444','1'))
cur.execute("INSERT INTO student (student_id, school, grade_level) VALUES (?,?,?)",('84','555','3'))

cur.execute("INSERT INTO course (teacher_id, course_id, name) VALUES (?,?,?)",('1','362','John'))
cur.execute("INSERT INTO course (teacher_id, course_id, name) VALUES (?,?,?)",('2','342','Lucy'))
cur.execute("INSERT INTO course (teacher_id, course_id, name) VALUES (?,?,?)",('3','322','Bob'))

cur.execute("INSERT INTO course_work (course_id, title) VALUES (?,?)",('362','Mathematics'))
cur.execute("INSERT INTO course_work (course_id, title) VALUES (?,?)",('342','Science'))
cur.execute("INSERT INTO course_work (course_id, title) VALUES (?,?)",('322','ELA'))

connection.commit()
connection.close()