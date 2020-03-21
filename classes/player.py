import json

class Player:
    name = ''
    life = 0
    xp = 0
    money = 0 # TODO
    clothes = ['top', 'jeans', 'hat', 'shoes']  # TODO: implement a weather system
    tools = ['gun'] # TODO
    food_stock = {'berries': 0} # TODO: Fix

    def player(self):
        with open('txt/saves/save' + self + '.json', 'r') as json_file:
            json_data = json.load(json_file)
            return json_data