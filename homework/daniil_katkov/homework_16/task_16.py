import csv
import os
import mysql.connector as mysql
import dotenv
import collections

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('DB'),
    ssl_disabled=False
)

cursor = db.cursor(dictionary=True)

select_all_information = '''
SELECT students.name, students.second_name, `groups`.title as group_title, books.title as book_title,
subjets.title as subject_title, lessons.title as lesson_title, marks.value as mark_value FROM students
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
'''

cursor.execute(select_all_information)
all_information = cursor.fetchall()

my_path = os.path.dirname(__file__)
file_data = os.path.dirname(os.path.dirname(my_path))
path_to_file = os.path.join(file_data, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(path_to_file, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    new_file = []
    for line in file_data:
        new_file.append(line)

db_list = [item for element in all_information for item in element.values()]
no_elements = collections.defaultdict(list)
for item in new_file:
    for key, values in item.items():
        if values not in db_list:
            no_elements[key].append(values)

no_elements = dict(no_elements)
print(no_elements)
