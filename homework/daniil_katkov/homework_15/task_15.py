import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

new_student = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
cursor.execute(new_student, ('Dan', 'Kat'))
student_id = cursor.lastrowid

new_books = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(new_books, [('Python history', student_id), ('Selenium history', student_id)])
cursor.execute(f"SELECT * FROM books WHERE taken_by_student_id = {student_id}")
my_books = cursor.fetchall()
book1_id = my_books[0]['id']
book2_id = my_books[1]['id']

new_group = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
cursor.execute(new_group, ('First class', 'nov 2024', 'may 2025'))
group_id = cursor.lastrowid

cursor.execute(f"UPDATE students SET group_id = {group_id} WHERE id = {student_id}")

new_subjects = "INSERT INTO subjets (title) VALUES (%s)"
cursor.executemany(new_subjects, [('Selenium (basic)',), ('Selenium (advanced)',)])
cursor.execute("SELECT * FROM subjets ORDER BY id DESC LIMIT 0, 2")
my_subjects = cursor.fetchall()
subject1_id = my_subjects[0]['id']
subject2_id = my_subjects[1]['id']

new_lessons = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
cursor.executemany(
    new_lessons, [
        ('Requests (part 1)', subject1_id),
        ('Requests (part 2)', subject2_id),
        ('Locust (part 1)', subject1_id),
        ('Locust (part 2)', subject2_id)
    ]
)
cursor.execute("SELECT * FROM lessons ORDER BY id DESC LIMIT 0, 4")
my_lessons = cursor.fetchall()
lesson1_id_part_1 = my_lessons[0]['id']
lesson1_id_part_2 = my_lessons[1]['id']
lesson2_id_part_1 = my_lessons[2]['id']
lesson2_id_part_2 = my_lessons[3]['id']

new_marks = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    new_marks, [
        (5, lesson1_id_part_1, student_id),
        (4, lesson1_id_part_2, student_id),
        (5, lesson2_id_part_1, student_id),
        (4, lesson2_id_part_2, student_id)
    ]
)
cursor.execute("SELECT * FROM marks ORDER BY id DESC LIMIT 0, 4")
my_marks = cursor.fetchall()
my_marks_id_1 = my_marks[0]['id']
my_marks_id_2 = my_marks[1]['id']
my_marks_id_3 = my_marks[2]['id']
my_marks_id_4 = my_marks[3]['id']

db.commit()

# Имя и Фамилия студента, группа, книги, оценки с названиями занятий и предметов нашего студента
select_all_information = f'''
SELECT students.name, students.second_name, `groups`.title as group_title, books.title as book_title, marks.value,
lessons.title as lesson_title, subjets.title as subject_title FROM students
JOIN books
ON students.id = books.taken_by_student_id
JOIN `groups`
ON students.group_id = `groups`.id
JOIN marks
ON students.id = marks.student_id
JOIN lessons
ON students.id = marks.student_id AND marks.lesson_id = lessons.id
JOIN subjets
ON students.id = marks.student_id AND marks.lesson_id = lessons.id AND lessons.subject_id = subjets.id
WHERE students.id = {student_id}
'''

cursor.execute(select_all_information)
print(cursor.fetchall())

db.close()
