from classes import *
import pdb, json, os, gettext, datetime

# TRANSLATIONS
fr = gettext.translation('fr_FR', localedir='i18n', languages=['fr'])
fr.install()

# Game characteristics
is_playing = True
weather = ['Sunny', 'Rainy']

# # Life index
# low_life = Player.life < 20
# mid_life = Player.life < 75
# full_life = Player.life <= 100
#
# CLEAR CONSOLE
os.system('cls')

Game.startGame()

if is_playing:
    print(_('\n\t##################################################################################################\n\n'
            '                             \t\tWhen you play, your game is auto saved.\n\n'
            '\t##################################################################################################\n'))

    date = datetime.datetime.strftime(datetime.date.today(), '%d/%m/%Y')
    time = datetime.datetime.strftime(datetime.datetime.now(), '%H:%M')

    # When player starts the game
    print(_('\n\tHey %s !\n'
            '\tIl est actuellement %s et nous sommes le %s.'
            '\n\tSi vous ne savez pas quoi faire, tapez simplement "help" !') % (Player.name, date, time))

# if low_life:
#     print(_('\tYou\'re weak. You only have %sLP.') % str(Player.life))
# elif mid_life:
#     print(_('\tTo my mind, you need to rest. You only have %sLP.') % str(Player.life))
# elif full_life:
#     print(_('\tToday is a good day. You have %sLP.') % str(Player.life))
#
actions = _('\n'
            '\t=========================\n'
            '\t   GAME ACTIONS:\n'
            '\t       - Eat\n'
            '\t       - Explore\n'
            '\t       - Craft\n'
            '\n'
            '\t   PLAYER ACTIONS:\n'
            '\t       - LP\n'
            '\t       - XP\n'
            '\t       - Money\n'
            '\t       - Inventory\n'
            '\t       - Get resources\n'
            '\t=========================\n')

# Player adventure
answer = ''
while answer != 'exit':
    answer = input(_('\nWhat do you wanna do?\n\t'))
    search = Functions.search_action(answer, Functions.actions)

    try:
        search
    except ValueError:
        print(_('\nWrong answer. Please try again.\n'))
    if answer == Functions.actions[0] or answer == Functions.actions_display[0]:
        print(actions)

    elif answer == Functions.actions[1] or answer == Functions.actions_display[1]:
        Feed.feed(Player)

    #     elif answer == Functions.actions[3] or answer == Functions.actions_display[3]:
    #         Explore.explore(Player, Functions, is_playing, game_save)
    #
    #     elif answer == Functions.actions[4] or answer == Functions.actions_display[4]:
    #         print(_('\nYou have %sLP.\n') % str(json_data['life']))
    #
    #     elif answer == Functions.actions[5] or answer == Functions.actions_display[5]:
    #         print(_('\nYou have %sxp.\n') % str(json_data['xp']))
    #
    #     elif answer == Functions.actions[6] or answer == Functions.actions_display[6]:
    #         print(_('\nYou have %s€.\n') % str(json_data['money']))
    #
    elif answer == Functions.actions[7] or answer == Functions.actions_display[7]:
        print(_('\nHere is your inventory:\n'))
        for elem in Player.inventory:
            print(_('\t' + elem))

    elif answer == Functions.actions[8] or answer == Functions.actions_display[8]:
        Ressources.getRessources()

    if answer == 'exit':
        Game.exitGame()
        is_playing = False
