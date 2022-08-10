import oper_numbers

# список допустимых операций с комплексными числами в калькуляторе
oper_rational = ['+', '-', '*', '/', '//', '%', 'sqrt', 'pow', 'abs']

# Ввод аргументов и типа операции для работы с рациональными числами в калькуляторе
def input_rational_numbers():
    try:
        arg1 = float(input('Введите число для выполнения операции: '))
    except:
        print('Ошибка ввода числа')
        return
    try:
        oper = input('Введите необходимую операцию (' + ', '.join(oper_rational) + '): ').strip()
        if oper == '+':
            arg2 = float(input('Введите второе слагаемое число: '))
            rez = oper_numbers.sum(arg1,arg2)
            print(f'Результат операции: {rez}')
        elif oper == '-':
            arg2 = float(input('Введите вычитаемое число: '))
            rez = oper_numbers.minus(arg1,arg2)
            print(f'Результат операции: {rez}')
        if oper == '*':
            arg2 = float(input('Введите множитель: '))
            rez = oper_numbers.multiplication(arg1,arg2)
            print(f'Результат операции: {rez}')
        elif oper == '/':
            arg2 = float(input('Введите делитель: '))
            rez = oper_numbers.division(arg1,arg2)
            print(f'Результат операции: {rez}')
        elif oper == '//':
            arg2 = float(input('Введите делитель для целочисленного деления: '))
            rez = oper_numbers.integer_division(arg1,arg2)
            print(f'Результат операции: {rez}')
        elif oper == '%':
            arg2 = float(input('Введите делитель для получения остатка от деления: '))
            rez = oper_numbers.remain_division(arg1,arg2)
            print(f'Результат операции: {rez}')
        elif oper == 'sqrt':
            rez = oper_numbers.sqrt(arg1)
            print(f'Результат операции: {rez}')
        elif oper == 'pow':
            arg2 = float(input('Введите число возводимой степени, например, 3 : '))
            rez = oper_numbers.exponentiation(arg1,arg2)
            print(f'Результат операции: {rez}')
        elif oper == 'abs':
            rez = oper_numbers.modul(arg1)
            print(f'Результат операции: {rez}')
        else:
            print(f'Ведена недопустимая операция {oper} с числами')
    except:
        print(f'Введенное число недопустимо для данной операции {oper}')
