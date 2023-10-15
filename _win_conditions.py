def win_cons_player_1(board: 'cls Board', y, x, player_1, player_2) -> bool:
    """ This function checks for the win conditions of the game Gomoku (Vietnamese version)"""

    "/ direction"
    count = 1
    blocked = 0
    for i in range(1, 100):

        if board.size[y + i][x - i] == ' ':
            break

        elif board.size[y + i][x - i] == player_1.symbol:
            count += 1

            if y + i == 0 or y + i == 15 or x - i == 0 or x - i == 15:
                break

        elif board.size[y + i][x - i] == player_2.symbol:
            blocked += 1
            break

    for i in range(1, 100):

        if board.size[y - i][x + i] == ' ':
            break

        elif board.size[y - i][x + i] == player_1.symbol:
            count += 1

            if y - i == 0 or y - i == 15 or x + i == 0 or x + i == 15:
                break

        elif board.size[y - i][x + i] == player_2.symbol:
            blocked += 1
            break

    if count == 5 and blocked != 2:
        return True

    return False


def win_cons_player_2(board: 'cls Board', y, x, player_1, player_2) -> bool:
    " / direction "
    count = 1
    blocked = 0
    for i in range(1, 100):

        if y == 0 or y == 14 or x == 0 or x == 14:
            break

        if board.size[y + i][x - i] == ' ':
            break

        elif board.size[y + i][x - i] == player_2.symbol:
            count += 1

            if y + i == 0 or y + i == 14 or x - i == 0 or x - i == 14:
                break

        elif board.size[y + i][x - i] == player_1.symbol:
            blocked += 1
            break

    for i in range(1, 100):

        if y == 0 or y == 14 or x == 0 or x == 14:  # Check for edges
            break

        if board.size[y - i][x + i] == ' ':
            break

        elif board.size[y - i][x + i] == player_2.symbol:
            count += 1

            if y - i == 0 or y - i == 14 or x + i == 0 or x + i == 14:  # Check for edges
                break

        elif board.size[y - i][x + i] == player_1.symbol:
            blocked += 1
            break

    if count == 5 and blocked != 2:
        return True

    return False

# Abort, might be unnecessarily complicated
