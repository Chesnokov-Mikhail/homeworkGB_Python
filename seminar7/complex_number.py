import oper_numbers

# список допустимых операций с комплексными числами в калькуляторе
oper_complex = ['+', '-', '*', '/', 'abs', 'sqrt', 'pow']

# Ввод аргументов и типа операции для работы с комплексными числами в калькуляторе
def input_complex_numbers():
    try:
        com1 = complex(input('Введите для выполнения операции комплексное число (a + bj), например, 2-5j : '))
    except:
        print('Введенное число не может быть представленно в виде комплексного числа')
        return
    try:
        oper = input('Введите необходимую операцию (' + ', '.join(oper_complex) + '): ').strip()
        if oper == '+':
            com2 = complex(input('Введите второе слагаемое число, например, 1+5j или 5.78 : '))
            rez = oper_numbers.sum(com1,com2)
            print(f'Результат операции: {rez}')
        elif oper == '-':
            com2 = complex(input('Введите вычитаемое число, например, 1+5j или 5.78 : '))
            rez = oper_numbers.minus(com1,com2)
            print(f'Результат операции: {rez}')
        if oper == '*':
            com2 = complex(input('Введите множитель, например, 1+5j или 5.78 : '))
            rez = oper_numbers.multiplication(com1,com2)
            print(f'Результат операции: {rez}')
        elif oper == '/':
            com2 = complex(input('Введите делитель, например, 1+5j или 5.78 : '))
            rez = oper_numbers.division(com1,com2)
            print(f'Результат операции: {rez}')
        elif oper == 'sqrt':
            rez = oper_numbers.sqrt(com1)
            print(f'Результат операции: {rez}')
        elif oper == 'pow':
            com2 = int(input('Введите число возводимой степени, например, 3 : '))
            rez = oper_numbers.exponentiation(com1,com2)
            print(f'Результат операции: {rez}')
        elif oper == 'abs':
            rez = oper_numbers.modul(com1)
            print(f'Результат операции: {rez}')
        else:
            print(f'Ведена недопустимая операция {oper} с комплексными числами')
    except:
        print(f'Введенное число недопустимо для данной операции {oper}')

