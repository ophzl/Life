import json

with open('txt/saves.json') as json_file:
    json = json.load(json_file)


class Player:
    json = json # For future save

    name = 'Ophélie'
    life = 100
    xp = json['1']['xp']
    money = json['1']['money'] # TODO
    clothes = ['top', 'jeans', 'hat', 'shoes']  # TODO: implement a weather system
    tools = ['gun'] # TODO
    food_stock = {'berries': 0} # TODO: Fix

    # Life index
    low_life = life < 20
    mid_life = life < 75
    full_life = life <= 100

    def display_LP(self):
        print('\nYou have ' + str(self.life) + 'LP.\n')

    def display_XP(self):
        print('\nYou have ' + str(self.xp) + 'XP.\n')

    def display_money(self):
        print('\nYou have ' + str(self.money) + '€.\n')

    # def display_food_stock(self):
    #     for key, value in self.food_stock.values():
    #         print('You have ' + value + ' ' + key)
