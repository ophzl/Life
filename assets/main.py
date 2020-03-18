import pdb

# Is game started ?
is_playing = True

# Character information
name = 'Valerie'
life = 15

# Game
actions_display = ['Help', 'Eat', 'Sleep']
actions = []

def to_lower(self):
    for k in self:
        index = self.index(k)
        result = self[index].lower()
        actions.append(result)

while is_playing:

    # When player start the game
    print('\nHello, ' + name)
    if life < 20:
        print('You\'re weak. You only have ' + str(life) + 'LP.')
    elif life < 50:
        print('To my mind, you need to rest. You only have ' + str(life) + 'LP.')
    elif life <= 100:
        print('Today is a good day. You have ' + str(life) + 'LP.')

    print('\n'
          '===================\n'
          '   You can...\n'
          '     1 - Eat\n'
          '     2 - Sleep\n'
          '===================')

    # Player choice
    answer = -1
    try:
        while answer != 'exit':
            answer = input('What do you wanna do?')
            # if answer.lower() in actions:

    except ValueError:
        print('Wrong answer. Please try again.')
        continue
    except AssertionError:
        print('Wrong answer. Please try again.')
        continue
