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
cursor.execute(new_books, ('Python history', student_id))
book1_id = cursor.lastrowid
cursor.execute(new_books, ('Selenium history', student_id))
book2_id = cursor.lastrowid

new_group = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
cursor.execute(new_group, ('First class', 'nov 2024', 'may 2025'))
group_id = cursor.lastrowid

cursor.execute(f"UPDATE students SET group_id = {group_id} WHERE id = {student_id}")

new_subjects = "INSERT INTO subjets (title) VALUES (%s)"
cursor.execute(new_subjects, ('Selenium (basic)',))
subject1_id = cursor.lastrowid
cursor.execute(new_subjects, ('Selenium (advanced)',))
subject2_id = cursor.lastrowid

new_lessons = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
cursor.execute(new_lessons, ('Requests (part 1)', subject1_id))
lesson_id_requests_1 = cursor.lastrowid
cursor.execute(new_lessons, ('Requests (part 2)', subject2_id))
lesson_id_requests_2 = cursor.lastrowid
cursor.execute(new_lessons, ('Locust (part 1)', subject1_id))
lesson_id_locust_1 = cursor.lastrowid
cursor.execute(new_lessons, ('Locust (part 2)', subject2_id))
lesson_id_locust_2 = cursor.lastrowid

new_marks = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.execute(new_marks, (5, lesson_id_requests_1, student_id))
my_marks_id_1 = cursor.lastrowid
cursor.execute(new_marks, (4, lesson_id_requests_2, student_id))
my_marks_id_2 = cursor.lastrowid
cursor.execute(new_marks, (5, lesson_id_locust_1, student_id))
my_marks_id_3 = cursor.lastrowid
cursor.execute(new_marks, (4, lesson_id_locust_2, student_id))
my_marks_id_4 = cursor.lastrowid

db.commit()

# Имя и Фамилия студента, группа, книги, оценки с названиями занятий и предметов нашего студента
select_all_information = '''
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
WHERE students.id = %s
'''

cursor.execute(select_all_information, (student_id,))
print(cursor.fetchall())

db.close()
