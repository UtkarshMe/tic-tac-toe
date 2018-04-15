#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import player
import util
import human

player1 = player.Player(1)
player2 = player.Player(2)
turn = 1
game_state = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

while True:

    # show game state
    print(game_state[0])
    print(game_state[1])
    print(game_state[2])
    print(turn)

    # check win
    win = util.check_win(game_state)
    if win:
        print('Player', win, 'wins!')
        break

    # player's turn
    if turn == 1:
        pos = player1.take_turn()
        player2.update_state(pos)
        turn = 2;
        pass

    # opponent's turn
    else:
        pos = player2.take_turn()
        player1.update_state(pos)
        turn = 1;
        pass
