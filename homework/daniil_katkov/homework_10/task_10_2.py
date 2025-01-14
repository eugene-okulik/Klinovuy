def repeat_me(func):
    def wrapper(x, **kwargs):
        second = 0
        result = list(kwargs.items())
        for b in result[-1]:
            second = b
        my_number = 0
        while my_number < second:
            func(x)
            my_number +=1
    return wrapper


@repeat_me
def example(text):
    print(text)

example('print me', count=2)

#########################################################


def repeat_me(count = 2):
    def my_example(func):
        def wrapper(*args, **kwargs):
            a = 0
            while a < count:
                func(*args, **kwargs)
                a +=1
        return wrapper
    return my_example


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')
