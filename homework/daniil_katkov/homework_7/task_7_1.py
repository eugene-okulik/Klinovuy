responce = 5
user_responce = int(input('You need to try to guess the hidden number from 1 to 10: '))

while user_responce != responce:
    user_responce = int(input('Try one more time: '))
print('Congrats! You are right!')

##############################################################################################

while True:
    response_user = int(input('You need to try to guess the hidden number from 1 to 10: '))
    if response_user == responce:
        print('Congrats! You are right!')
        break
    else:
        print('Try one more time')
