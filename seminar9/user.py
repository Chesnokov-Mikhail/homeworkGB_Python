import games

# анализ координат, введенных пользователем
def user_input(pole, arg):
    try:
        (user_in_line,user_in_column) = [int(x) for x in arg]
    except:
        return 'Необходимо ввести целые числа!'
    else:
        if games.check_coordinates(pole, (user_in_line, user_in_column)):
            return (user_in_line, user_in_column)
        else:
            return 'Указанная ячейка занята, выбирете другую: '