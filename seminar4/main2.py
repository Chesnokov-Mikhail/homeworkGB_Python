'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд
с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой

Вывод программы необходимо оформить следующим образом:
Команда:Всегоигр Побед Ничьих Поражений Всегоочков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.

Sample Input:

3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15
Sample Output:

Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
'''

def input_result_games(n):
    sp_result_games = []
    try:
        for i in range(0, n):
            result_games = input('Введите результаты игры в следующем формате, '
                                '"Первая команда";"Забито первой командой";'
                                '"Вторая команда";"Забито второй командой": ').split(';')
            if len(result_games) < 4:
                raise
            # преобразуем забитые голы в int
            for j in (1, 3):
                result_games[j] = int(result_games[j])
            sp_result_games.append(result_games)
    except:
        print('Результаты игр необходимо вводить по формату')
    return sp_result_games

def union_table_games(sp_games):
    table_games = {}

    for game in sp_games:
        result_game_1 = table_games.setdefault(game[0], [0, 0, 0, 0, 0])
        result_game_2 = table_games.setdefault(game[2], [0, 0, 0, 0, 0])
        result_game_1[0] += 1
        result_game_2[0] += 1
        if game[1] > game[3]:
            result_game_1[4] += 3
            result_game_1[1] += 1
            result_game_2[3] += 1
        elif game[1] == game[3]:
            result_game_1[4] += 1
            result_game_2[4] += 1
            result_game_1[2] += 1
            result_game_2[2] += 1
        else:
            result_game_2[4] += 3
            result_game_2[1] += 1
            result_game_1[3] += 1

        table_games[game[0]] = result_game_1
        table_games[game[2]] = result_game_2

    return table_games

def view_union_table(union_table):
    print('Команда: "Всего игр" "Побед" "Ничьих" "Поражений" "Всего очков"')
    for (key, value) in union_table.items():
        print('{}: {}'.format(key, ' '.join([str(item) for item in value])))

if __name__ == '__main__':
    try:
        nn = int(input('Введите количество завершенных игр (целое число): '))
        view_union_table(union_table_games(input_result_games(nn)))
    except:
        print('Введите целое число завершенных игр')


