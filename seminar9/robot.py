from random import choice
import games

# Выбор ячейки поля ботом
def robot_game():
    coordinate = choice(games.pole_game_var)
    return coordinate


