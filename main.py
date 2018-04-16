#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import player
import util
import human

player1 = player.Player(1)
player2 = human.Player(2)
turn = 1
game_state = [0, 0, 0, 0, 0, 0, 0, 0, 0 ]

while True:

    # show game state
    print(game_state[0], game_state[1], game_state[2])
    print(game_state[3], game_state[4], game_state[5])
    print(game_state[6], game_state[7], game_state[8])
    print()

    # check win
    win = util.check_win(game_state)
    if win:
        print('Player', win, 'wins!')
        break

    pos = -1

    # player's turn
    if turn == 1:
        pos = player1.take_turn()
        if pos == -1:
            break
        player2.update_state(pos)
        game_state[pos] = 1
        turn = 2;
        pass

    # opponent's turn
    else:
        pos = player2.take_turn()
        if pos == -1:
            break
        game_state[pos] = 2
        player1.update_state(pos)
        turn = 1;
        pass
