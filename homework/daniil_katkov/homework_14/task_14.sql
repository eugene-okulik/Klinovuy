INSERT INTO students (name, second_name) VALUES ('Daniil', 'Katkov')

INSERT INTO books (title, taken_by_student_id) VALUES ('My Python', 4317)
INSERT INTO books (title, taken_by_student_id) VALUES ('QA manual', 4317)

INSERT INTO `groups` (title, start_date, end_date) VALUES ('Python group', 'nov 2024', 'may 2025')

UPDATE students SET group_id = 2720 WHERE name = 'Daniil' and second_name = 'Katkov'

INSERT INTO subjets (title) VALUES ('Playwright for beginner')
INSERT INTO subjets (title) VALUES ('Selenium for beginner')

INSERT INTO lessons (title, subject_id) VALUES ('Playwright part 1', 4376)
INSERT INTO lessons (title, subject_id) VALUES ('Playwright part 2', 4376)
INSERT INTO lessons (title, subject_id) VALUES ('Selenium part 1', 4377)
INSERT INTO lessons (title, subject_id) VALUES ('Selenium part 2', 4377)

INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 8138, 4317)
INSERT INTO marks (value, lesson_id, student_id) VALUES (4, 8139, 4317)
INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 8140, 4317)
INSERT INTO marks (value, lesson_id, student_id) VALUES (4, 8141, 4317)


SELECT * FROM marks WHERE student_id = 4317

SELECT * FROM books WHERE taken_by_student_id = 4317

SELECT * FROM students
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
WHERE students.name = 'Daniil' and students.second_name = 'Katkov'