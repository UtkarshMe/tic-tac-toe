import random

class KnowledgeBase():
    def __init__(self):
        self.rules = []
        self.atoms = {
            'E': [1, 1, 1, 1, 1, 1, 1, 1, 1],
            'X': [0, 0, 0, 0, 0, 0, 0, 0, 0],
            'O': [0, 0, 0, 0, 0, 0, 0, 0, 0],
            'W': [0, 0, 0, 0, 0, 0, 0, 0, 0],
            'L': [0, 0, 0, 0, 0, 0, 0, 0, 0],
        }
        self.atoms_size = 9

        def rule(atoms):
            for x in range(0, self.atoms_size):
                if atoms['X'][x] == 1 or atoms['O'][x] == 1:
                    atoms['E'][x] = 0
        self.rules.append(rule)

        def gen_win(rules, a, b, c):
            def rule(atoms):
                if atoms['E'][a] == 1 and atoms['X'][b] == 1 and atoms['X'][c] == 1:
                    atoms['W'][a] = 1
            rules.append(rule)
            def rule(atoms):
                if atoms['X'][a] == 1 and atoms['E'][b] == 1 and atoms['X'][c] == 1:
                    atoms['W'][b] = 1
            rules.append(rule)
            def rule(atoms):
                if atoms['X'][a] == 1 and atoms['X'][b] == 1 and atoms['E'][c] == 1:
                    atoms['W'][c] = 1
            rules.append(rule)
            def rule(atoms):
                if atoms['E'][a] == 1 and atoms['O'][b] == 1 and atoms['O'][c] == 1:
                    atoms['L'][a] = 1
            rules.append(rule)
            def rule(atoms):
                if atoms['O'][a] == 1 and atoms['E'][b] == 1 and atoms['O'][c] == 1:
                    atoms['L'][b] = 1
            rules.append(rule)
            def rule(atoms):
                if atoms['O'][a] == 1 and atoms['O'][b] == 1 and atoms['E'][c] == 1:
                    atoms['L'][c] = 1
            rules.append(rule)

        gen_win(self.rules, 0, 1, 2)
        gen_win(self.rules, 3, 4, 5)
        gen_win(self.rules, 6, 7, 8)

        gen_win(self.rules, 0, 3, 6)
        gen_win(self.rules, 1, 4, 7)
        gen_win(self.rules, 2, 5, 8)

        gen_win(self.rules, 0, 4, 8)
        gen_win(self.rules, 2, 4, 6)


    def percept(self, position):
        self.atoms['O'][position] = 1
        self.atoms['W'] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.atoms['L'] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for func in self.rules:
            func(self.atoms)
        pass

    def actuate(self):
        # check for empty
        flag = 0
        for index in self.atoms['E']:
            if index == 1:
                flag = 1
                break
        if flag == 0:
            return -1

        list_of_empty = self.atoms['E']

        # select winning move
        wins = []
        for index in range(0, self.atoms_size):
            if self.atoms['W'][index] == 1:
                wins.append(index)
        if len(wins) != 0:
            self.atoms['X'][wins[0]] = 1
            return wins[0]

        # select blocking move to prevent losing
        loses = []
        for index in range(0, self.atoms_size):
            if self.atoms['L'][index] == 1:
                loses.append(index)
        if len(loses) != 0:
            self.atoms['X'][loses[0]] = 1
            return loses[0]

        # select random move
        while True:
            move = random.randint(0, 8)
            if list_of_empty[move] == 1:
                self.atoms['X'][move] = 1
                return move
