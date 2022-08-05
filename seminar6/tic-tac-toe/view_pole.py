def view_pole_game(pole):
    size = len(pole)
    print('{0:<3}{1:_^7}{2:_^7}{3:_^7}'.format('',1,2,3))
    for i in range(0, size):
        print(f'{i+1:<3}', end='')
        for j in range(0, size):
            print('{0}{1:_^5}'.format('|',pole[i][j]), end='|')
        print()