import util

class Player():
    """The Human who plays"""

    def __init__(self, mark):
        self.mark = mark

    def take_turn(self, state):
        while True:
            x = int(input())
            y = int(input())
            if state[x][y] == 0:
                state[x][y] = self.mark
                break
            print('Occupied')
