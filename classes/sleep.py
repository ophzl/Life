class Sleep:
    def sleep(self):
        if self.life != 100:
            if self.low_life:
                print('\nYou sleep very well and gain 20LP.')
            if self.mid_life:
                print('\nYou sleep and gain 15LP.')
            if self.full_life:
                print('\nEven if you\'re almost full life, you gain 5LP.')
        else:
            print('\nHaha ! You don\'t need to sleep !')