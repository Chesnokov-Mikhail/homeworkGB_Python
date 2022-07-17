'''
Напишите проамму, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
пусть N 4: тогда [1, 2, 6, 24] (1, 1*2, 1*2*3, 1*1*3*4)
'''

def multiply_numbers(num):
    sp = []
    n = 1
    for i in range(1, num + 1):
        n = n*i
        sp.append(n)
    return sp

if __name__ == '__main__':
    try:
        str_num = input('Введите целое число: ')
        num = int(str_num)
        print(f'Пусть N = {num}, тогда ', multiply_numbers(num))
    except:
        print('Введите целое число!')
