import random

class Player():
    """The Player who plays"""

    def __init__(self, mark):
        self.mark = mark
        pass

    def take_turn(self, state):

        # TODO: make it intelligent
        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if state[x][y] == 0:
                state[x][y] = self.mark
                break

        pass

