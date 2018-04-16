def check_win(state):
    win = 0
    def winner(x, y, z):
        if state[x] == state[y] and state[y] == state[z]:
            return state[x]

    win = winner(0, 1, 2)
    if win: return win
    win = winner(3, 4, 5)
    if win: return win
    win = winner(6, 7, 8)
    if win: return win

    win = winner(0, 3, 6)
    if win: return win
    win = winner(1, 4, 7)
    if win: return win
    win = winner(2, 5, 8)
    if win: return win

    win = winner(0, 4, 8)
    if win: return win
    win = winner(2, 4, 6)
    if win: return win

    return 0
