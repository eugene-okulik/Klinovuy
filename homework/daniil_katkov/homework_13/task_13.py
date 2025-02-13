import os
import datetime


my_path = os.path.dirname(__file__)
file_data = os.path.dirname(os.path.dirname(my_path))
path_to_file = os.path.join(file_data, 'eugene_okulik', 'hw_13', 'data.txt')

with open(path_to_file) as teacher_file:
    new_file = teacher_file.read()
    one_line = new_file.splitlines()
    first_line, second_line, third_line = one_line


def format_date(line):
    only_date = (line[line.index('.') + 1:line.index('- ')]).strip(' ')
    python_date = datetime.datetime.strptime(only_date, '%Y-%m-%d %H:%M:%S.%f')
    if line == first_line:
        print(python_date + datetime.timedelta(days=7))
    elif line == second_line:
        print(python_date.strftime('%A'))
    else:
        now = datetime.datetime.now()
        days_ago = (now - python_date).days
        print(f'{days_ago} дней назад')


format_date(third_line)


#######################################################################################################


import os
import datetime


my_path = os.path.dirname(__file__)
file_data = os.path.dirname(os.path.dirname(my_path))
file_path = os.path.join(file_data, 'eugene_okulik', 'hw_13', 'data.txt')

with open(file_path) as file:
    lines = file.readlines()


def process_line(line):
    parts = line.split(" - ")
    number, date_str = parts[0].split(". ")
    action = parts[1].strip()
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
    if number == "1":
        print(date + datetime.timedelta(days=7))
    elif number == "2":
        print(date.strftime("%A"))
    elif number == "3":
        now = datetime.datetime.now()
        days_diff = (now - date).days
        print(f"{days_diff} дней назад")


for line in lines:
    process_line(line)
