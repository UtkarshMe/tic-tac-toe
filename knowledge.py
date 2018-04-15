class KnowledgeBase():
    def __init__(self):
        self.rules = []
        self.atoms = {
            'E': [1, 1, 1, 1, 1, 1, 1, 1, 1],
            'X': [0, 0, 0, 0, 0, 0, 0, 0, 0],
            'O': [0, 0, 0, 0, 0, 0, 0, 0, 0],
            'W': [0, 0, 0, 0, 0, 0, 0, 0, 0],
        }

        def rule(atoms, x):
            if atoms['X'][x] == 1 or atoms['O'][x] == 1:
                atoms['E'][x] = 0
        self.rules.append(rule)

        def gen_win(rules, a, b, c):
            def rule(atoms, x):
                if atoms['E'][a] == 1 and atoms['X'][b] == 1 and atoms['X'][c] == 1:
                    atoms['W'][a] = 1
            rules.append(rule)
            def rule(atoms, x):
                if atoms['X'][a] == 1 and atoms['E'][b] == 1 and atoms['X'][c] == 1:
                    atoms['W'][b] = 1
            rules.append(rule)
            def rule(atoms, x):
                if atoms['X'][a] == 1 and atoms['X'][b] == 1 and atoms['E'][c] == 1:
                    atoms['W'][c] = 1
            rules.append(rule)

        gen_win(self.rules, 0, 1, 2)
        gen_win(self.rules, 3, 4, 5)
        gen_win(self.rules, 6, 7, 8)

        gen_win(self.rules, 0, 3, 6)
        gen_win(self.rules, 1, 4, 7)
        gen_win(self.rules, 2, 5, 8)

        gen_win(self.rules, 0, 4, 8)
        gen_win(self.rules, 3, 4, 6)


    def percept(self, position):
        for func in self.rules:
            func(self.atoms, position)
        pass

    def actuate(self):
        print(self.atoms)
        return 0
