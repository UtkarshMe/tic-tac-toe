import random
import util
import knowledge

class Player():
    """The Player who plays"""

    def __init__(self, mark):
        self.mark = mark
        self.kb = KnowledgeBase();
        pass

    def get_max(self, current_state):
        curr = util.deserialize(current_state, self.mark)
        try:
            opts = self.kb[curr]
        except Exception as e:
            return random.randint(0, 2), random.randint(0, 2)
        return opts[0], opts[1]

    def take_turn(self, state):
        while True:
            x, y = self.get_max(state);
            if state[x][y] == 0:
                state[x][y] = self.mark
                break
