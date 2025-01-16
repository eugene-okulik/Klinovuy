number_one = int(input('Введите первое число: '))
number_two = int(input('Введите второе число: '))


def operations(func):
    def wrapper(first, second):
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        elif first < 0 or second < 0:
            operation = '*'
        else:
            return 'Error'
        return func(first, second, operation)
    return wrapper


@operations
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second
    else:
        return 'Error'


result = calc(number_one, number_two)
print(result)
