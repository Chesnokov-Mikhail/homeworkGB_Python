pole_game_var = []

def pole_game_init(size: int):
    global pole_game_var
    pole_game_var = [(i,j) for j in range(1, size+1) for i in range(1, size+1)]
    return [['' for j in range(0, size)] for i in range(0, size)]

def pole_game_mark(pole: list, coordinates: tuple, mark: str):
    global pole_game_var
    i, j = coordinates
    pole_game_var.remove((i, j))
    pole[i - 1][j - 1] = mark

def game_end() -> bool:
    global pole_game_var
    if len(pole_game_var) == 0:
        return True
    return False

def check_coordinates(pole: list, coordinates: tuple) -> bool:
    (i, j) = coordinates
    try:
        if pole[i - 1][j - 1] != '':
            return False
    except:
        return False
    else:
        return True

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
