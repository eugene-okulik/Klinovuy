str_1 = 'результат операции: 42'
str_2 = 'результат операции: 54'
str_3 = 'результат работы программы: 209'
str_4 = 'результат: 2'


def sum(str_0):
    str_number = str_0.index(':') + 2
    str_sum = int(str_0[str_number:]) + 10
    print(str_sum)


sum(str_4)

############################################################


def sum(str_0):
    str_number = str_0.split()
    last_element = int(str_number[-1]) + 10
    print(last_element)


sum(str_3)
