from classes import *
import pdb, json, os

# Game characteristics
is_playing = True
weather = ['Sunny', 'Rainy']

# Save 1
with open('txt/saves/save1.json', 'r') as json_file:
    json_data = json.load(json_file)
    name1 = json_data['name']

# Save 2
with open('txt/saves/save2.json', 'r') as json_file:
    json_data = json.load(json_file)
    name2 = json_data['name']

# Save 3
with open('txt/saves/save3.json', 'r') as json_file:
    json_data = json.load(json_file)
    name3 = json_data['name']

# CLEAR CONSOLE
os.system('clear')

# Saves
saves = [1, 2, 3]
save = input('\n\t      Choose a save:\n'
             '\t      1 - ' + name1 +
             '\n\t      2 - ' + name2 +
             '\n\t      3 - ' + name3 + '\n')

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

if Player.player(game_save)['name'] != '':
    Player.name = Player.player(game_save)['name']
    Player.life = Player.player(game_save)['life']
    Player.xp = Player.player(game_save)['xp']
    Player.money = Player.player(game_save)['money']
else:
    with open('txt/saves/save'+ game_save +'.json', 'r') as json_file:
        json_data = json.load(json_file)
    json_data['name'] = input('\nOh, you\'re new. What\'s your name?\n\t')
    with open('txt/saves/save'+ game_save +'.json', 'w') as json_file:
        json.dump(json_data, json_file)
    Player.name = Player.player(game_save)['name']
    Player.life = Player.player(game_save)['life']
    Player.xp = Player.player(game_save)['xp']
    Player.money = Player.player(game_save)['money']

# Life index
low_life = Player.life < 20
mid_life = Player.life < 75
full_life = Player.life <= 100

# CLEAR CONSOLE
os.system('clear')

# Advert msg
print('\n\t##################################################################################################\n\n'
      '                             \t\tWhen you play, your game is auto saved.\n\n'
      '\t##################################################################################################\n')

# When player starts the game
# TODO: add datetime to say different kind of msg according to the hour of the day
print('\n\tHey ' + Player.name + '\n')

if low_life:
    print('\tYou\'re weak. You only have ' + str(Player.life) + 'LP.')
elif mid_life:
    print('\tTo my mind, you need to rest. You only have ' + str(Player.life) + 'LP.')
elif full_life:
    print('\tToday is a good day. You have ' + str(Player.life) + 'LP.')

display_actions = ('\n'
                   '\t=========================\n'
                   '\t      You can...\n'
                   '\t        Eat\n'
                   '\t        Sleep\n'
                   '\t        Explore\n'
                   '\n'
                   '\t More actions -> \'help\'\n'
                   '\t=========================\n')

print(display_actions)

more_actions = ('\n'
                '\t=========================\n'
                '\t   GAME ACTIONS:\n'
                '\t       - Eat\n'
                '\t       - Sleep\n'
                '\t       - Explore\n'
                '\n'
                '\t   PLAYER ACTIONS:\n'
                '\t       - LP\n'
                '\t       - XP\n'
                '\t       - Money\n'
                '\t=========================\n')

# Player adventure
answer = ''
while answer != 'exit':
    with open('txt/saves/save'+ game_save +'.json', 'r') as json_file:
        json_data = json.load(json_file)
    answer = input('What do you wanna do?\n\t')
    search = Functions.search_action(answer, Functions.actions)
    try:
        search
    except ValueError:
        print('Wrong answer. Please try again.\n')
    if answer == Functions.actions[0] or answer == Functions.actions_display[0]:
        print(more_actions)

    if answer == Functions.actions[1] or answer == Functions.actions_display[1]:
        Feed.feed(Player)

    elif answer == Functions.actions[2] or answer == Functions.actions_display[2]:
        Sleep.sleep(Player, game_save)

    elif answer == Functions.actions[3] or answer == Functions.actions_display[3]:
        Explore.explore(Player, Functions, is_playing, game_save)

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
