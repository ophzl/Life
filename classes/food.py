import json
from . import Functions

class Feed:
    def feed(self):
        search = Functions.search_action('Meat', self.inventory)
        if search and self.foodPoints < 100:
            print(_('(+50FP) What a good feeling...'))
            self.foodPoints += 50
            self.inventory.pop()
        elif not search:
            print(_('You don\'t have enough food !'))

        elif self.foodPoints == 100:
            print(_('Vous n\'avez pas besoin de manger.'))