class Functions:
    actions_display = ['Help', 'Eat', 'Sleep', 'Explore']
    actions = []

    # Function to display an array in lower
    def to_lower(self, array):
        for k in self:
            index = self.index(k)
            result = self[index].lower()
            array.append(result)

    to_lower(actions_display, actions)

    # Function verify if player choice exists
    def search_action(self, actions):
        for k in range(len(actions)):
            if actions[k] == self:
                return True
        return False