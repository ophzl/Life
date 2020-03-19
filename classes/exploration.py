import main, time, random
from classes import Functions


class Explore:
    explore = []
    is_exploring = False

    def explore(self):
        print('\nExploring the world.\n')
        continue_exploration = ''
        is_exploring = True

        while is_exploring:
            when_exploring = random.randrange(1, 3)
            continue_exploration = input('Do you want to continue ? (yes/no)\n')

            if when_exploring == 1:
                print('Oh no! You does the malin and felt in the ravin. You loose 25LP.')
                self.life -= 15
            elif when_exploring == 2:
                animals = ['Rat', 'Crocodile', 'Bull']
                print('You\'re in front of a big and mysterious animal...\n')
                time.sleep(3)
                print('...we can distinguish it\'s...')
                time.sleep(1)
                print('...a ' + random.choice(animals) + '!')
                time.sleep(1)
                choices = ['Fight', 'Run']
                choices_lower = []

                Functions.to_lower(choices, choices_lower)

                self_choice = input('What do you do ?\n'
                                      'Fight\n'
                                      'Run')
            elif when_exploring == 3:
                print('3')

            if continue_exploration == 'no':
                is_exploring = False

            if self.life == 0:
                print('You\'re dead.')
                is_exploring = False
                main.is_playing = False

            if continue_exploration == 'no':
                is_exploring = False