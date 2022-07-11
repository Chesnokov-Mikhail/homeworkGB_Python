'''
3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
 плоскости, в которой находится эта точка (или на какой оси она находится).
 *Пример:*
 - x=34; y=-30 -> 4
- x=2; y=4-> 1
 - x=-34; y=-30 -> 3
'''


def get_quatro_plane(x, y):
    if x > 0 and y > 0:
        plane = 1
    elif x < 0 and y > 0:
        plane = 2
    elif x < 0 and y < 0:
        plane = 3
    else:
        plane = 4
    return plane


if __name__ == '__main__':
    try:
        x_point = float(input('Введите координату точки X: '))
        y_point = float(input('Введите координату точки Y: '))
    except:
        print('Необходимо ввести число')
    if x_point != 0 and y_point != 0:
        print('x = {}; y = {} -> {}'.format(x_point, y_point, get_quatro_plane(x_point, y_point)))
