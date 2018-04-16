def check_win(state):
    return False
    for i in range(0, 3):

        if (state[i][0] and state[i][0] == state[i][1] and state[i][0] == state[i][2]):
            return state[i][0];

        if (state[0][i] and state[0][i] == state[1][i] and state[0][i] == state[2][i]):
            return state[0][i];

    if (state[0][0] and state[0][0] == state[1][1] and state[1][1] == state[2][2]):
        return state[0][0]

    if (state[0][2] and state[0][2] == state[1][1] and state[1][1] == state[2][0]):
        return state[0][2]

    flag = True
    for i in range(0, 3):
        for j in range(0, 3):
            if state[i][j] == 0:
                flag = False
                break
    if flag:
        return 'no one'


def deserialize(state, mark):
    result = ""
    for i in range(0, 3):
        for j in range(0, 3):
            if state[i][j] == mark:
                result += '1';
            elif state[i][j] == 0:
                result += '0';
            else:
                result += '2';
    return result
