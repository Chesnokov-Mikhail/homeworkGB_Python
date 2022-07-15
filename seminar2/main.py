'''
Напишите программу, которая на вход принимает вещественное число и показывает сумму его цифр
Пример:
 - 6782 ->23
 - 0,56 -> 11
'''
'''
не рабочий вариант, т.к. значение вещественного числа после запятой представляется в машинном виде,
большим количеством цифр, которые при округлении дают заданное число  
'''
def summ_digits_number(num, lengt):
    summ = 0
    num_int = int(num)
    num_float = num - num_int
    for i in range(0,lengt):
        # сумма цифр целой части числа
        if num_int > 0:
            summ += num_int % 10
            num_int = num_int // 10
        else:
        # сумма цифр после запятой
            num_float = num_float * 10
            summ += int(num_float)
            num_float = num_float - int(num_float)
    return summ

def summ_digits_str(num):
    num_list = num.split('.')
    summ = 0
    for num_i in num_list:
        for i in num_i:
            summ += int(i)
    return summ


if __name__ == '__main__':
    try:
        str_num = input('Введите число (целое или вещественное): ')
#        count = len(str_num)
        num = float(str_num)
    except:
        print('Введите число!')
#    print(f'- {num} -> ', summ_digits_number(num, count))
    print(f'- {str_num} -> ', summ_digits_str(str_num))
