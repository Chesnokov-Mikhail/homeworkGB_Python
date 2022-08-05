'''
Создайте программу для игры в "Крестики-нолики".
Размерность поля 3х3
'''
import view_pole as view
import games
import robot
import user
from random import randint

if __name__ == '__main__':
    try:
        size = int(input('Введите целое число, размер поля: '))
    except:
        print('Введено не целое число')
    else:
        pole = games.pole_game_init(size)
        view.view_pole_game(pole)
        game_exit = False
        # Кто первый ходит, робот (0) или пользователь (1)
        next_move = randint(0, 1)
        if not next_move:
            print('Первым ходит робот')
        while not game_exit:
            if next_move:
                mark = 'X'
                user_move = user.user_input(pole)
                if user_move:
                    (i, j) = user_move
                else:
                    continue
            else:
                mark = '0'
                robot_move = robot.robot_game(pole)
                (i, j) = robot_move
            next_move = not next_move
            games.pole_game_mark(pole, (i, j), mark)
            view.view_pole_game(pole)
            if games.check_game_win(pole, mark):
                print(f'{mark} выйграли')
                game_exit = True
            else:
                game_exit = games.game_end()
                if game_exit:
                    print('Ига окончена, все ячейки заполнены')