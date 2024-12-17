def gen():
    start = 0
    start_1 = 1
    while True:
        yield start
        start, start_1 = (start_1, start + start_1)


fib_numbers = []

selected_values = [5, 200, 1000, 100000]

count = 1
for element in gen():
    if count in selected_values:
        fib_numbers.append(element)
    if count == selected_values[-1]:
        break
    count += 1

print(fib_numbers)

####################################################################


def gen():
    start = 0
    start_1 = 1
    while True:
        yield start
        start, start_1 = (start_1, start + start_1)


selected_values = [5, 200, 1000, 100000]

count = 1
for element in gen():
    if count in selected_values:
        print(element)
    if count == selected_values[-1]:
        break
    count += 1
