import main


class Functions:
    # Function to display an array in lower
    def to_lower(self, array):
        for k in self:
            index = self.index(k)
            result = self[index].lower()
            array.append(result)

    # Function verify if player choice exists
    def search_action(self):
        for k in range(len(main.actions)):
            if main.actions[k] == main.answer:
                return True
        return False