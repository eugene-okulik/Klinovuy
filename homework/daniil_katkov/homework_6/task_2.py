for element in range(1, 101):
    if (element/5).is_integer() and (element/3).is_integer():
        print('FuzzBuzz')
    elif (element/3).is_integer():
        print('Fuzz')
    elif (element/5).is_integer():
        print('Buzz')
    else:
        print(element)

print('#########################################')

for element in range(1, 101):
    if element % 3 == 0 and element % 5 == 0:
        print('FuzzBuzz')
    elif element % 3 == 0:
        print('Fuzz')
    elif element % 5 == 0:
        print('Buzz')
    else:
        print(element)
