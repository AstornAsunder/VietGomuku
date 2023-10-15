"""
Main script to play the game
"""

__Author__ = 'Lam Khuu'

# import tkinter
import os
from the_players import *
from the_board import Board
from gc import collect

import collections
# from pprint import pprint

def main():
    # os.system('cmd /k "python Gomoku.py"')

    """ main function"""

    def clear():
        os.system('cls')

    "Declare and instantiate variables"
    board = Board()
    player_1 = Player(input('Player 1\'s name: '), 'X')
    player_2 = Player(input('Player 2\'s name: '), 'O')
    #if player_1.name == player_2.name:

    valid_input = list(range(1, len(board.size) + 1))
    print(valid_input)
    game_on = True
    while game_on:
        board.display_board()

        " Players take turn and play. Algo checks for win con every move."
        while True:

            """ Player 1's turn """

            a = f"{player_1.name}'s turn"
            print(f"{a:^30}")
            del a
            collect()

            while True:
                try:
                    y1_input, x1_input = player_input()
                except ValueError:
                    print("Invalid input...")
                    continue
                if y1_input not in valid_input or x1_input not in valid_input:
                    print("Invalid position...")
                    continue

                y1 = y1_input - 1  # x_input,y_input -> display | x,y -> index board.size
                x1 = x1_input - 1

                if board.size[y1][x1] == ' ':
                    board.size[y1][x1] = player_1.symbol
                    break
                else:
                    print("The position has been taken. Choose a different position.")

            board.display_board()
            " Check for win conditions "

            # / direction:
            count = 1
            blocked = 0
            for i in range(1, 100):  # + -

                if y1_input + i == 16 or x1_input - i == 0:
                    break

                match board.size[y1 + i][x1 - i]:
                    case ' ':
                        break
                    case player_1.symbol:
                        count += 1
                        if y1 + i == 14 or x1 - i == 0:
                            break
                    case player_2.symbol:
                        blocked += 1
                        break

            for i in range(1, 100):  # - +

                if y1_input - i == 0 or x1_input + i == 16:
                    break

                match board.size[y1 - i][x1 + i]:
                    case ' ':
                        break
                    case player_1.symbol:
                        count += 1
                        if y1 - i == 0 or x1 + i == 14:
                            break
                    case player_2.symbol:
                        blocked += 1
                        break

            if count == 5 and blocked != 2:
                player_1.wins()
                break

            # — direction:
            count = 1
            blocked = 0
            for i in range(1, 100):  # -

                if x1_input - i == 0:
                    break

                match board.size[y1][x1 - i]:
                    case ' ':
                        break
                    case player_1.symbol:
                        count += 1
                        if x1 - i == 0:
                            break
                    case player_2.symbol:
                        blocked += 1
                        break

            for i in range(1, 100):  # +

                if x1_input + i == 16:
                    break

                match board.size[y1][x1 + i]:
                    case ' ':
                        break
                    case player_1.symbol:
                        count += 1
                        if x1 + i == 14:
                            break
                    case player_2.symbol:
                        blocked += 1
                        break

            if count == 5 and blocked != 2:
                player_1.wins()
                break

            # \ direction
            count = 1
            blocked = 0
            for i in range(1, 100):  # - -

                if y1_input - i == 0 or x1_input - i == 0:
                    break

                match board.size[y1 - i][x1 - i]:
                    case ' ':
                        break
                    case player_1.symbol:
                        count += 1
                        if y1 - i == 0 or x1 - i == 0:
                            break
                    case player_2.symbol:
                        blocked += 1
                        break

            for i in range(1, 100):  # + +

                if y1_input + i == 16 or x1_input + i == 16:
                    break

                match board.size[y1 + i][x1 + i]:
                    case ' ':
                        break
                    case player_1.symbol:
                        count += 1
                        if y1 + i == 14 or x1 + i == 14:
                            break
                    case player_2.symbol:
                        blocked += 1
                        break

            if count == 5 and blocked != 2:
                player_1.wins()
                break

            # | direction:
            count = 1
            blocked = 0
            for i in range(1, 100):  # -

                if y1_input - i == 0:
                    break

                match board.size[y1 - i][x1]:
                    case ' ':
                        break
                    case player_1.symbol:
                        count += 1
                        if y1 - i == 0:
                            break
                    case player_2.symbol:
                        blocked += 1
                        break

            for i in range(1, 100):  # +

                if y1_input + i == 16:
                    break

                match board.size[y1 + i][x1]:
                    case ' ':
                        break
                    case player_1.symbol:
                        count += 1
                        if y1 + i == 14:
                            break
                    case player_2.symbol:
                        blocked += 1
                        break

            if count == 5 and blocked != 2:
                player_1.wins()
                break

            """ Player 2's turn """

            a = f"{player_2.name}'s turn"
            print(f"{a:^30}")
            del a
            collect()

            while True:
                try:
                    y2_input, x2_input = player_input()
                except ValueError:
                    print("Invalid input...")
                    continue
                if y2_input not in valid_input or x2_input not in valid_input:
                    print("Invalid position...")
                    continue

                y2 = y2_input - 1  # x_input,y_input -> display | x,y -> index board.size
                x2 = x2_input - 1

                if board.size[y2][x2] == ' ':
                    board.size[y2][x2] = player_2.symbol
                    break
                else:
                    print("The position has been taken. Choose a different position.")

            board.display_board()

            # break
            " Check for win conditions "

            # / direction:
            count = 1
            blocked = 0
            for i in range(1, 100):  # + -

                if y2_input + i == 16 or x2_input - i == 0:
                    break

                match board.size[y2 + i][x2 - i]:
                    case ' ':
                        break
                    case player_2.symbol:
                        count += 1
                        if y2 + i == 14 or x2 - i == 0:
                            break
                    case player_1.symbol:
                        blocked += 1
                        break

            for i in range(1, 100):  # - +

                if y2_input - i == 0 or x2_input + i == 16:
                    break

                match board.size[y2 - i][x2 + i]:
                    case ' ':
                        break
                    case player_2.symbol:
                        count += 1
                        if y2 - i == 0 or x2 + i == 14:
                            break
                    case player_1.symbol:
                        blocked += 1
                        break

            if count == 5 and blocked != 2:
                player_2.wins()
                break

            # — direction:
            count = 1
            blocked = 0
            for i in range(1, 100):  # -

                if x2_input - i == 0:
                    break

                match board.size[y2][x2 - i]:
                    case ' ':
                        break
                    case player_2.symbol:
                        count += 1
                        if x2 - i == 0:
                            break
                    case player_1.symbol:
                        blocked += 1
                        break

            for i in range(1, 100):  # +

                if x2_input + i == 16:
                    break

                match board.size[y2][x2 + i]:
                    case ' ':
                        break
                    case player_2.symbol:
                        count += 1
                        if x2 + i == 14:
                            break
                    case player_1.symbol:
                        blocked += 1
                        break

            if count == 5 and blocked != 2:
                player_2.wins()
                break

            # \ direction
            count = 1
            blocked = 0
            for i in range(1, 100):  # - -

                if y2_input - i == 0 or x2_input - i == 0:
                    break

                match board.size[y2 - i][x2 - i]:
                    case ' ':
                        break
                    case player_2.symbol:
                        count += 1
                        if y2 - i == 0 or x2 - i == 0:
                            break
                    case player_1.symbol:
                        blocked += 1
                        break

            for i in range(1, 100):  # + +

                if y2_input + i == 16 or x2_input + i == 16:
                    break

                match board.size[y2 + i][x2 + i]:
                    case ' ':
                        break
                    case player_2.symbol:
                        count += 1
                        if y2 + i == 14 or x2 + i == 14:
                            break
                    case player_1.symbol:
                        blocked += 1
                        break

            if count == 5 and blocked != 2:
                player_2.wins()
                break

            # | direction:
            count = 1
            blocked = 0
            for i in range(1, 100):  # -

                if y2_input - i == 0:
                    break

                match board.size[y2 - i][x2]:
                    case ' ':
                        break
                    case player_2.symbol:
                        count += 1
                        if y2 - i == 0:
                            break
                    case player_1.symbol:
                        blocked += 1
                        break

            for i in range(1, 100):  # +

                if y2_input + i == 16:
                    break

                match board.size[y2 + i][x2]:
                    case ' ':
                        break
                    case player_2.symbol:
                        count += 1
                        if y2 + i == 14:
                            break
                    case player_1.symbol:
                        blocked += 1
                        break

            if count == 5 and blocked != 2:
                player_2.wins()
                break

        p1score = f"{player_1.name}'s current score"
        p2score = f"{player_2.name}'s current score"
        print(f"{p1score:^32}|{p2score:^32}")
        print(f"{player_1.score:^32}|{player_2.score:^32}")
        del p1score, p2score

        next_round = input('Next round? Y or N: ')
        if next_round == 'Y':
            board.reset_board()
        elif next_round == 'N':
            game_on = False
        del next_round

        collect()

    if player_1.score > player_2.score:
        print(f"{player_1.name} victory!")
    elif player_1.score < player_2.score:
        print(f"{player_2.name} victory!")
    else:
        print("It's a tie!")


if __name__ == '__main__':
    main()

# board
# display board
# handle turn
# check win cons:
# check rows
# check columns
# check diagonals
# Check for edges with [0] and [-1] and opponent's marks
#
# check tie (tie when less than 5 positions are available)

"""code fragments:"""
