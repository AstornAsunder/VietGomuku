"""
A script for creating a Board Class
"""


from pprint import pprint


class Board:

    def __init__(self, num_row=15, num_column=15):

        """ Make a 15x15 board by default """

        # This code below results in a glitch
        self.size = []
        for _ in range(num_row):
            self.size.append([' '] * num_column)

    def display_board(self):

        """ Display the board """

        print('0    ', end='')
        for i in range(1, 16):
            print(f'{i:^6}', end='')  # print and number the x-axis
        print('')

        vertical_border = '|'
        i = 1
        for row in range(15):
            print(f'{i:<4}{vertical_border}', end='')  # print and number the y-axis
            for col in range(15):
                print(f"{self.size[row][col]:^5}{vertical_border}", end='')
            print('')
            i += 1

    def reset_board(self):
        self.__init__()
