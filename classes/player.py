from classes import *

class Player:
    name = list()
    life = 100
    xp = 0
    money = 0  # TODO: implement a money system
    clothes = ['top', 'jeans', 'hat', 'shoes']  # TODO: implement a weather system
    guns = []  # TODO: implement a guns system

    # Life index
    low_life = life < 20
    mid_life = life < 50
    full_life = life <= 100