import games

def view_pole_game():
    size = len(games.pole)
    view_pole = f'{"":_<4}'
    for i in range(0, size):
        view_pole += f'{i+1:_^6}'
    view_pole += '\n'
    for i in range(0, size):
        view_pole += f'{i+1:<3} '
        for j in range(0, size):
            view_pole +='{0}{1:_^5}'.format('|',games.pole[i][j])
        view_pole += '|\n'
    return view_pole