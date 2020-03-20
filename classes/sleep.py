import json
class Sleep:
    def sleep(self):
        if self.life != 100:
            if self.low_life:
                print('\n(+20LP) || You sleep very well and gain 20LP.\n')
                self.life += 20
            elif self.mid_life:
                print('\n(+15LP) || You sleep and gain 15LP.\n')
                self.life += 15
            elif self.full_life:
                print('\n(+5LP) || Even if you\'re almost full life, you gain 5LP.\n')
                self.life += 5

        else:
            print('\nHaha ! You don\'t need to sleep !\n')