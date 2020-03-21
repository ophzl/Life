import json

class Sleep:
    def sleep(self):
        with open('txt/saves/save1.json', 'r') as json_file:
            json_data = json.load(json_file)
            life = json_data['life']
            if life < 100:
                if life < 20:
                    print('\n(+20LP) || You sleep very well and gain 20LP.\n')
                    life += 20
                elif life < 75:
                    print('\n(+15LP) || You sleep and gain 15LP.\n')
                    json_data['life'] += 15
                elif life < 100:
                    print('\n(+5LP) || Even if you\'re almost full life, you gain 5LP.\n')
                    json_data['life'] += 5

            else:
                print('\nHaha ! You don\'t need to sleep !\n')

        with open('txt/saves/save1.json', 'w') as json_file:
            json.dump(json_data, json_file)