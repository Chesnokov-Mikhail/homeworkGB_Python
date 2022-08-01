'''
Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность.
Порядок элементов менять нельзя.
Пример:
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
[1, 5, 2, 3, 4, 1, 7] => [1, 5]
'''

'''
Вариант 2. Методом перебора исходного списка, в найденных возрастающих последовательностях находится
           максимально длинная последовательность 
вход: список для поиска наибольшей возрастающей последовательности
выход: список наибольшей возрастающей последовательности
'''
def find_sub_increment(sp_init: list):
    dict_inc = {}
    sp_sub = []
    for (i, n) in enumerate(sp_init):
        if i not in sp_sub:
            sp_sub.append(i)
            count_inc = 1
            min_inc = n
            max_inc = n
            count_minus = 1
            while True:
                sp_sub_minus = [j for (j, num) in enumerate(sp_init) if (num == (n - count_minus) and j not in sp_sub)]
                if sp_sub_minus:
                    sp_sub.extend(sp_sub_minus)
                    min_inc = n - count_minus
                    count_minus += 1
                    count_inc += 1
                else:
                    break
            count_plus = 1
            while True:
                sp_sub_plus = [j for (j, num) in enumerate(sp_init) if (num == (n + count_plus) and j not in sp_sub)]
                if sp_sub_plus:
                    sp_sub.extend(sp_sub_plus)
                    max_inc = n + count_plus
                    count_plus += 1
                    count_inc += 1
                else:
                    break
            if count_inc > 1:
                dict_inc[count_inc] = [min_inc, max_inc]
    if dict_inc.keys():
        nvp = max(dict_inc.keys())
        return dict_inc[nvp]
    else:
        return []

'''
Вариант 1. Методом динамического программирования
вход: список для поиска наибольшей возрастающей последовательности
выход: список наибольшей возрастающей последовательности
'''
def find_subsequence_increment(sp_init: list):
    sp_inc = [1]*len(sp_init)
    sp = sorted(sp_init)
    for i in range(len(sp)):
        for j in range(i):
            if sp[j] + 1 == sp[i]:
                if sp_inc[j] >= sp_inc[i]:
                    sp_inc[i] = sp_inc[j] + 1
    return [sp[sp_inc.index(min(sp_inc))], sp[sp_inc.index(max(sp_inc))]]

if __name__ == '__main__':
    sp = [1, 5, 2, 3, 4, 6, 1, 7]
    #sp = [1, 5, 2, 3, 4, 1, 7]
    print('Вариант 1')
    print(sp, ' => ', find_subsequence_increment(sp))
    print('Вариант 2')
    print(sp, ' => ', find_sub_increment(sp))