from classes import *
import pdb, json

# Game characteristics
is_playing = True
weather = ['Sunny', 'Rainy']

# Saves
saves = [1, 2, 3]
save = input('\nChoose a save:\n'
             '      1\n'
             '      2\n'
             '      3\n')

search = Functions.search_action(save, saves)
game_save = '0'

try:
    save = int(save)
except ValueError:
    print('Wrong answer. Please try again.\n')

if save == saves[0]:
    game_save = '1'
elif save == saves[1]:
    game_save = '2'
elif save == saves[2]:
    game_save = '3'

Player.name = Player.player(game_save)['name']
Player.life = Player.player(game_save)['life']
Player.xp = Player.player(game_save)['xp']
Player.money = Player.player(game_save)['money']

# Life index
low_life = Player.life < 20
mid_life = Player.life < 75
full_life = Player.life <= 100

# When player starts the game
# TODO: add datetime to say different kind of msg according to the hour of the day
print('\nHey ' + Player.name + '\n')

if low_life:
    print('You\'re weak. You only have ' + str(Player.life) + 'LP.')
elif mid_life:
    print('To my mind, you need to rest. You only have ' + str(Player.life) + 'LP.')
elif full_life:
    print('Today is a good day. You have ' + str(Player.life) + 'LP.')

display_actions = ('\n'
                   '=========================\n'
                   '      You can...\n'
                   '        Eat\n'
                   '        Sleep\n'
                   '        Explore\n'
                   '\n'
                   ' More actions -> \'help\'\n'
                   '=========================\n')

print(display_actions)

more_actions = ('\n'
                '=========================\n'
                '   GAME ACTIONS:\n'
                '       - Eat\n'
                '       - Sleep\n'
                '       - Explore\n'
                '\n'
                '   PLAYER ACTIONS:\n'
                '       - LP\n'
                '       - XP\n'
                '       - Money\n'
                '       - Food Stock\n'
                '=========================\n')

# Player adventure
answer = ''
while answer != 'exit':
    with open('txt/saves/save1.json', 'r') as json_file:
        json_data = json.load(json_file)
    answer = input('What do you wanna do?\n')
    search = Functions.search_action(answer, Functions.actions)
    while not search:
        print('Wrong answer. Please try again.\n')
        search = Functions.search_action(answer, Functions.actions)
        answer = input('What do you wanna do?\n')
    if answer == Functions.actions[0] or answer == Functions.actions_display[0]:
        print(more_actions)

    if answer == Functions.actions[1] or answer == Functions.actions_display[1]:
        Feed.feed(Player)

    elif answer == Functions.actions[2] or answer == Functions.actions_display[2]:
        Sleep.sleep(Player)

    elif answer == Functions.actions[3] or answer == Functions.actions_display[3]:
        Explore.explore(Player, Functions, is_playing)

    elif answer == Functions.actions[4] or answer == Functions.actions_display[4]:
        print('\nYou have ' + str(json_data['life']) + 'LP.\n')

    elif answer == Functions.actions[5] or answer == Functions.actions_display[5]:
        print('\nYou have ' + str(json_data['xp']) + 'xp.\n')

    elif answer == Functions.actions[6] or answer == Functions.actions_display[6]:
        print('\nYou have ' + str(json_data['money']) + '€.\n')

    # elif answer == Functions.actions[7] or answer == Functions.actions_display[7]:
    #     pdb.set_trace()
    #     Player.display_food_stock(Player)

    if answer == 'exit':
        print('Right, goodbye!')
        is_playing = False
