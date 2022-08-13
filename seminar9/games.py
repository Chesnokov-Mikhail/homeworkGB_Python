# Матрица ячеек игрового поля для выбора ботом доступного хода
pole_game_var = []
# Матрица игрового поля для маркировки хода
pole = []
# переменная для хранения последней команды
old_command = ''
# Признак начала игры
game_start = False
# Признак конца игры
game_exit = False
# Кто ходит, робот (0) или пользователь (1)
next_move = 1

def init_games():
    global old_command
    global game_exit
    global game_start
    global pole_game_var
    global pole

    old_command = '/start'
    game_exit = False
    game_start = True
    pole_game_var = []
    pole = []

# инициализация игрового поля
def pole_game_init(size: int):
    global pole_game_var
    pole_game_var = [(i,j) for j in range(1, size+1) for i in range(1, size+1)]
    return [['' for j in range(0, size)] for i in range(0, size)]

# установка метки на игровом поле при очередном ходе
def pole_game_mark(coordinates: tuple, mark: str):
    global pole_game_var
    global pole
    i, j = coordinates
    pole_game_var.remove((i, j))
    pole[i - 1][j - 1] = mark

# проверка на конец игры
def game_end(mark):
    global pole
    global game_exit
    if check_game_win(pole, mark):
        game_exit = True
        return f'{mark} выйграли'
    else:
        game_exit = full_mark_pole()
        if game_exit:
             return 'Ига окончена, все ячейки заполнены'

# проверка на заполненность всех ячеек игрового поля
def full_mark_pole() -> bool:
    global pole_game_var
    global game_exit
    if len(pole_game_var) == 0:
        game_exit = True
        return True
    return False

# проверка занятости ячейки
def check_coordinates(pole: list, coordinates: tuple) -> bool:
    (i, j) = coordinates
    try:
        if pole[i - 1][j - 1] != '':
            return False
    except:
        return False
    else:
        return True

# проверка победителя
def check_game_win(pole, mark) -> bool:
    size = len(pole)
    chek_column = [True for i in range(0, size)]
    chek_diagonal = [True for i in range(0, 2)]
    for i in range(0, size):
        chek_line = True
        # проверка заполнения диагоналей маркером
        if pole[i][i] != mark :
            chek_diagonal[0] = False
        if pole[i][size - i - 1] != mark:
            chek_diagonal[1] = False
        # проверка заполнения строки одним маркером
        for j in range(0, size):
            if pole[i][j] != mark:
                chek_line = False
                # отмечаем какой столбец не заполнен одним маркером
                chek_column[j] = False
        # если строка заполнена одним маркером
        if chek_line:
            return True
    # Если есть заполненная диагональ одним маркером или столбец
    result = (True if True in chek_diagonal else False) or (True if True in chek_column else False)
    return result
