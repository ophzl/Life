from . import Player
from . import Functions
import json, time, os

with open('txt/saves/save1.json', 'r') as json_file:
    json_data = json.load(json_file)


class Game:

    def startGame():
        choices = [1, 2]
        game_choice = input(_('\t      Chose your game:\n'
                              '\t      1 - %s' % json_data['name'] +
                              '\n\n\t 2 - === CREATE NEW GAME ===\n\n'))

        search = Functions.search_action(game_choice, choices)

        try:
            game_choice = int(game_choice)
        except ValueError:
            print(_('Wrong answer. Please try again.\n'))

        if game_choice == 1:
            Game.loadPlayer('1')
        else:
            confirmation = input(_('Are you sure you want to erase the actual save ? (this action is irreversible)\n'))
            if confirmation == 'yes':
                game_creation = True
                Game.createPlayer('1', game_creation)
                Game.loadPlayer('1')
            else:
                return False

    def createPlayer(self, game_creation):
        difficulties = [1, 2, 3]

        json_data['name'] = input(_('\nOh, you\'re new. What\'s your name?\n\t'))
        json_data['life'] = 100
        json_data['foodPoints'] = 100
        json_data['xp'] = 0
        json_data['money'] = 0
        json_data['food'] = 0

        while game_creation:
            json_data['difficulty'] = input(_('\nChose your difficulty:\n'
                                              '\t1 - Easy'
                                              '\n\t2 - Medium'
                                              '\n\t3 - Hard\n\n'))
            search = Functions.search_action(json_data['difficulty'], difficulties)

            try:
                json_data['difficulty'] = int(json_data['difficulty'])
                game_creation = False
            except ValueError:
                print(_('Wrong answer. Please try again.\n'))

            starter = input(_('\nDo you want to start with a starter pack ?\n'))

            if starter == 'yes':
                json_data['inventory'] = ['Wood Sword', 'Wood Axe', 'Wood Pickaxe']
                print(_('\nYou\'ve been equiped with a wood sword, a wood axe and a wood pickaxe.'))
            else:
                return False

            print(_('\nHere are the parameters of your game:\n'
                    '\t Your name: %s\n'
                    '\t Your difficulty: %s\n'
                    '\t Starter pack: %s\n' % (json_data['name'], json_data['difficulty'], starter)))
            time.sleep(3)

            print(_('\n\n\t=== Explications ==='
                    '\n\tVotre partie est automatiquement sauvegardée. Aucune action de votre part n\'est nécessaire.'
                    '\n\tA tout moment, vous pouvez visualiser les actions disponibles en tapant "help".'
                    '\n\tLes points de vie sont symbolisés par des "LP" (Life Points).'
                    '\n\tLes points de nourriture sont symbolisés par des "FP" (Food Points).'
                    '\n\tLe seul moyen d\'obtenir des objets de haut niveau est de tomber sur une ville lors d\'un voyage. Ces objets peuvent être acquis en échange d\'argent.'
                    '\n\tIl vous est possible d\'obtenir de l\'argent en fabriquant une fonderie et en y faisant fondre de l\'or que vous aurez préalablement miné.'))
            time.sleep(15)

            print(_('\n\nLa partie va commencer...\n\n'))
            time.sleep(3)

        with open('txt/saves/save' + self + '.json', 'w') as json_file:
            json.dump(json_data, json_file)

    def loadPlayer(self):
        os.system('cls')
        with open('txt/saves/save' + self + '.json', 'r') as json_file:
            json_data = json.load(json_file)
        Player.name = json_data['name']
        Player.life = json_data['life']
        Player.foodPoints = json_data['foodPoints']
        Player.xp = json_data['xp']
        Player.money = json_data['money']
        Player.inventory = json_data['inventory']

    def exitGame():
        with open('txt/saves/save1.json', 'r') as json_file:
            json_data = json.load(json_file)
        json_data['life'] = Player.life
        json_data['foodPoints'] = Player.foodPoints
        json_data['xp'] = Player.xp
        json_data['money'] = Player.money
        json_data['inventory'] = Player.inventory

        with open('txt/saves/save1.json', 'w') as json_file:
            json.dump(json_data, json_file)

        print(_('Partie sauvegardée. A bientôt !'))
