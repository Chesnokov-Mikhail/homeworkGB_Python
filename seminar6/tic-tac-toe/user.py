import games

def user_input(pole):
    try:
        user_in_line = int(input('Введите номер строки: '))
        user_in_column = int(input('Введите номер столбца: '))
    except:
        print('Необходимо ввести целые числа!')
    else:
        if games.check_coordinates(pole, (user_in_line, user_in_column)):
            return (user_in_line, user_in_column)
        else:
            print('Указанная ячейка занята, выбирете другую: ')
            return False
