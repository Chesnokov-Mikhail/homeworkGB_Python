'''
1. Задайте список. Напишите программу, которая определит,
присутствует ли в заданном списке строк некое число.
'''

def is_digit_for_sp(sp):
    for i in sp:
        if i.isnumeric():
            return True
    return False

if __name__ == '__main__':
    sp = ['опуаоа', 'fwev', 'dksjcvkl', 'sdjkvhsk', 'efiknv']
    #sp = ['опуаоа', 'fwev', 'dksjcvkl', '95', 'efiknv']
    #sp = ['опууааоа', 'fweedcv', '3.4', '34', 'efваiknv']
    print('В списке: {} {}'.format(sp, 'есть число.' if is_digit_for_sp(sp) else 'нет чисел.'))