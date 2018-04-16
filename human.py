import util

class Player():
    """The Human who plays"""

    def __init__(self, mark):
        self.mark = mark

    def update_state(self, position):
        pass

    def take_turn(self):
        try:
            x = int(input())
            return x
        except:
            return self.take_turn()
