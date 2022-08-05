from random import choice
import games

def robot_game(pole):
    size = len(pole)
    try:
        coordinate = choice(games.pole_game_var)
    except:
        print('ходы закончились')
    else:
        return coordinate


