import json

class Feed:
    # TODO: implement a food system
    def feed(self, game_save):
        with open('txt/saves/save'+ game_save +'.json', 'r') as json_file:
            json_data = json.load(json_file)

        if json_data['food']:
            print(_('(+50FP) What a good feeling...'))
            json_data['food'] -= 50
            json_data['foodPoints'] += 50

        else:
            print(_('You don\'t have enough food !'))