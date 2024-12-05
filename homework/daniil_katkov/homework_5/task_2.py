result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'

result_for_1 = result_1.index('42')
int_result_1 = int(result_1[result_for_1:]) + 10

print(int_result_1)

result_for_2 = result_2.index('514')
int_result_2 = int(result_2[result_for_2:]) + 10

print(int_result_2)

result_for_3 = result_3.index('9')
int_result_3 = int(result_3[result_for_3:]) + 10

print(int_result_3)
