import random
import util
import knowledge

class Player():
    """The Player who plays"""

    def __init__(self, mark):
        self.mark = mark
        self.kb = knowledge.KnowledgeBase();

    def update_state(self, position):
        self.kb.percept(position)

    def take_turn(self):
        return self.kb.actuate()
