import random


while True:
    salary = input('Your salary: ')
    if salary.lower() == 'q':
        print('Good bye!')
        break
    salary = int(salary)
    sum = salary + random.randint(100, 300)
    bonus = random.choice([True, False])
    if bonus is True:
        print(f'{salary}, {bonus} - ${sum}')
    else:
        print(f'{salary}, {bonus} - ${salary}')
