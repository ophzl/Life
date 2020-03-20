from classes import *
import pdb

# Game characteristics
is_playing = True
weather = ['Sunny', 'Rainy']

while is_playing:
    # When player start the game
    prompt_name = input('What\'s your name ?\n')
    Player.name.append(prompt_name)

    # TODO: add datetime to say different kind of msg according to the hour of the day
    print('\nHey ' + Player.name[0] + '\n')

    if Player.low_life:
        print('You\'re weak. You only have ' + str(Player.life) + 'LP.')
    elif Player.mid_life:
        print('To my mind, you need to rest. You only have ' + str(Player.life) + 'LP.')
    elif Player.full_life:
        print('Today is a good day. You have ' + str(Player.life) + 'LP.')

    help_msg = ('\n'
                '=========================\n'
                '      You can...\n'
                '        Eat\n'
                '        Sleep\n'
                '        Explore\n'
                '\n'
                ' Need help ? Type \'help\'\n'
                '=========================')

    print(help_msg)

    # Player adventure
    answer = ''
    while answer != 'exit':
        answer = input('What do you wanna do?\n')
        search = Functions.search_action(answer, Functions.actions)
        while not search:
            print('Wrong answer. Please try again.\n')
            search = Functions.search_action(answer, Functions.actions)
            answer = input('What do you wanna do?\n')
        if answer == Functions.actions[0]:
            print(help_msg)

        if answer == Functions.actions[1]:
            Feed.feed(Player)

        elif answer == Functions.actions[2]:
            Sleep.sleep(Player)

        elif answer == Functions.actions[3]:
            Explore.explore(Player, Functions, is_playing)

        if answer == 'exit':
            print('Right, goodbye!')
            is_playing = False
