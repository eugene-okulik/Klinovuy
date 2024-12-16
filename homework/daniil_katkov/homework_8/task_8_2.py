def gen():
    start = 0
    start_1 = 1
    while True:
        yield start
        start, start_1 = (start_1, start + start_1)


fib_numbers = []


count = 1
for element in gen():
    if count == 1000:
        fib_numbers.append(element)
        print(fib_numbers)
        break
    count += 1
