import time, random


class Explore:
    is_exploring = False

    def explore(self, function, main):
        print('\nExploring the world...\n')
        is_exploring = True

        while is_exploring:
            when_exploring = random.randrange(1, 3)
            continue_exploration = input('Do you want to continue ? (yes/no)\n')
            if continue_exploration == 'no':
                is_exploring = False
            if is_exploring:
                if when_exploring == 1:
                    print('(-25LP) || Oh no! Who does the malin fall in the ravin. You loose 25LP.')
                    self.life -= 15
                elif when_exploring == 2:
                    animals = ['Rat', 'Crocodile', 'Bull', 'Wolf', 'Cow', 'Dog', 'Cat', 'Coronavirus']
                    print('\nYou\'re in front of a big and mysterious animal...')
                    time.sleep(3)
                    print('...we can distinguish it\'s...')
                    time.sleep(1)
                    print('...a ' + random.choice(animals) + '!\n')
                    time.sleep(1)
                    choices = ['Fight', 'Run']
                    choices_lower = []

                    function.to_lower(choices, choices_lower)

                    player_choice = input('What do you do ?\n'
                                          '   - Fight\n'
                                          '   - Run\n')
                    if player_choice == choices_lower[0]:
                        if self.xp < 50:
                            print('\nYou have 10% of chance to win.\n')
                            continue_fight = input('Are you sure you want to continue ? (yes/no)\n')
                            issue = ['win', 'loose']
                            if continue_fight != 'no':
                                chances = [0.1, 0.9]
                                result = random.choices(issue, chances)
                                if result == ['win']:
                                    print('(+15px) || You\'re really lucky. You win this fight and gain 15xp.')
                                    self.xp += 15
                                if result == ['loose']:
                                    print('(-25LP) || You loose... ')
                            elif continue_fight == 'no':
                                print('ok')

                elif when_exploring == 3:
                    print('3')

                if continue_exploration == 'no':
                    is_exploring = False

                if self.life == 0:
                    print('You\'re dead.')
                    is_exploring = False
                    main = False
