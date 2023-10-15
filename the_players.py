"""
A script for creating a Player class
"""

import time
import os


class Player:

    def __init__(self, name: str, symbol: "X or O", timer=315):
        self.name = name
        self.symbol = symbol
        self.timer = timer  # seconds or milliseconds? (seems to be in seconds)
        self.score = 0

    def wins(self):
        self.score += 1
        print(f"{self.name} wins!")

    def reset_timer(self, timer=315):
        self.timer = timer

def player_input():
    print("Position input (row x column): ")
    y, x = (input('Y: '), input('X: '))
    return int(y), int(x)

# player_1 = Player('haha','X')
#
#
# """Timer algorithm"""
#
# while player_1.timer:
#     mins = player_1.timer // 60
#     secs = player_1.timer % 60
#     print(f"\r {mins}:{secs}", end='')
#     time.sleep(1)
#     player_1.timer -= 1
#
# while player_2.timer:
#     mins = player_2.timer // 60
#     secs = player_2.timer % 60
#     print(f"\r {mins}:{secs}", end ='')
#     time.sleep(1)
#     player_2.timer -= 1
