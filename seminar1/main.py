'''
1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
    Пример:
 - 6 -> да
 - 7 -> да
 - 1 -> нет
'''


def is_weekday(day):
    if weekday == 6 or weekday == 7:
        return True
    else:
        return False


if __name__ == '__main__':
    in_day = input('Введите цифру, обозначающую день недели [1 - 7]: ')
    try:
        weekday = int(in_day)
    except:
        print('Необходимо ввести число')
    if (1 <= weekday <= 7):
        print(f'{weekday} -> Да') if is_weekday(weekday) else print(f'{weekday} -> Нет')
    else:
        print('Введите число из диапазона [1 - 7]')
