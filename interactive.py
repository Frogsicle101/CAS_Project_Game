class Lever:
    def __init__(self, action):
        self.action = action
    def getAction(self):
        return self.action()
