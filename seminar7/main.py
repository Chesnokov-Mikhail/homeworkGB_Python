import rational_number
import complex_number

if __name__ == '__main__':
    while True:
        print('Калькулятор')
        print('1. Работа с рациональными числами')
        print('2. Работа с комплексными числами')
        print('0. Выход из калькулятора')
        try:
            user_choice = int(input('Введите номер операции: '))
            if user_choice == 0:
                print('Выход из калькулятора')
                break
            elif user_choice == 1:
                rational_number.input_rational_numbers()
            elif user_choice == 2:
                complex_number.input_complex_numbers()
            else:
                raise
        except:
            print('Выберите нужный пункт меню')
