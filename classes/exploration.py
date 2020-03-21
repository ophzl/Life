import time, random, json


class Explore:
    is_exploring = False

    def explore(self, function, main, game_save):

        with open('txt/saves/save'+ game_save +'.json', 'r') as json_file:
            json_data = json.load(json_file)
        print('\nExploring the world...\n')

        is_exploring = True

        while is_exploring:

            when_exploring = random.randrange(1, 4)
            continue_exploration = input('Do you want to continue ? (yes/no)\n')

            if continue_exploration == 'no':
                is_exploring = False

            if is_exploring:

                if when_exploring == 1: # Ravin
                    print('(-25LP) || Oh no! Who does the malin fall in the ravin. You loose 25LP.')
                    json_data['life'] -= 15

                elif when_exploring == 2: # Animal
                    # TODO: add an external file where all animals are referenced with unique message for fight
                    animals_txt = open('txt/animals.txt', 'r')
                    animals = animals_txt.read().splitlines()

                    print('\nYou\'re in front of a big and mysterious animal...')
                    time.sleep(3)
                    print('...we can distinguish it\'s...')
                    time.sleep(1)
                    print('...a ' + random.choice(animals))
                    time.sleep(1)

                    choices = ['Fight', 'Run']
                    choices_lower = []

                    function.to_lower(choices, choices_lower)

                    player_choice = input('What do you do ?\n'
                                          '   - Fight\n'
                                          '   - Run\n')
                    # search = function.search_action(player_choice, choices_lower)
                    # while not search:
                    #     print('Wrong answer. Please try again.')
                    #     search = function.search_action(player_choice, choices_lower)
                    #     player_choice = input('What do you do ?\n'
                    #                           '   - Fight\n'
                    #                           '   - Run\n')
                    if player_choice == choices_lower[0]:
                        if json_data['xp'] < 50:
                            chances = [0.1, 0.9]
                            print('\nYou have 10% of chance to win.\n')
                            continue_fight = input('Are you sure you want to continue ? (yes/no)\n')
                            issue = ['win', 'loose']
                            if continue_fight != 'no':
                                result = random.choices(issue, chances)
                                if result == ['win']:
                                    print('(+50xp) || You\'re really lucky. You win this fight and gain 50xp.')
                                    json_data['xp'] += 50
                                if result == ['loose']:
                                    print('(-25LP) || You loose... ')
                                    json_data['life'] -= 25
                        elif json_data['xp'] < 100:
                            chances = [0.2, 0.8]
                            print('\nYou have 20% of chance to win.\n')
                            continue_fight = input('Are you sure you want to continue ? (yes/no)\n')
                            issue = ['win', 'loose']
                            if continue_fight != 'no':
                                result = random.choices(issue, chances)
                                if result == ['win']:
                                    print('(+50xp) || You\'re really lucky. You win this fight and gain 50xp.')
                                    json_data['xp'] += 50
                                if result == ['loose']:
                                    print('(-25LP) || You loose... ')
                                    json_data['life'] -= 25
                        elif json_data['xp'] < 150:
                            chances = [0.3, 0.7]
                            print('\nYou have 30% of chance to win.\n')
                            continue_fight = input('Are you sure you want to continue ? (yes/no)\n')
                            issue = ['win', 'loose']
                            if continue_fight != 'no':
                                result = random.choices(issue, chances)
                                if result == ['win']:
                                    print('(+50xp) || You\'re really lucky. You win this fight and gain 50xp.')
                                    json_data['xp'] += 50
                                if result == ['loose']:
                                    print('(-25LP) || You loose... ')
                                    json_data['life'] -= 25
                        elif json_data['xp'] < 200:
                            chances = [0.4, 0.6]
                            print('\nYou have 40% of chance to win.\n')
                            continue_fight = input('Are you sure you want to continue ? (yes/no)\n')
                            issue = ['win', 'loose']
                            if continue_fight != 'no':
                                result = random.choices(issue, chances)
                                if result == ['win']:
                                    print('(+50xp) || You\'re really lucky. You win this fight and gain 50xp.')
                                    json_data['xp'] += 50
                                if result == ['loose']:
                                    print('(-25LP) || You loose... ')
                                    json_data['life'] -= 25
                    if player_choice == choices_lower[1]:
                        print('\nYou run.\n')

                elif when_exploring == 3:
                    print('\n(+5 berries) || You found a bush full of berries.')
                    self.food_stock['berries'] += 5

                if continue_exploration == 'no':
                    is_exploring = False

                if json_data['life'] == 0:
                    print('You\'re dead.')
                    is_exploring = False
                    main = False

        with open('txt/saves/save'+ game_save +'.json', 'w') as json_file:
            json.dump(json_data, json_file)
