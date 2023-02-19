import random

class Sudoku:
    def __init__(self):
        self.board = self.generate_board()
        self.print_board()

    def generate_board(self):
        # create an empty board
        board = [[0 for j in range(9)] for i in range(9)]

        # fill the diagonal boxes with random numbers
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = []
                for k in range(1, 10):
                    box.append(k)
                random.shuffle(box)
                for x in range(3):
                    for y in range(3):
                        board[i+x][j+y] = box.pop()

        # fill the remaining cells using backtracking algorithm
        self.solve(board)

        # remove some cells to create a puzzle
        num_cells_to_remove = random.randint(40, 60)
        cells_removed = 0
        while cells_removed < num_cells_to_remove:
            i = random.randint(0, 8)
            j = random.randint(0, 8)
            if board[i][j] != 0:
                board[i][j] = 0
                cells_removed += 1

        return board

    def solve(self, board):
        find = self.find_empty(board)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.valid(board, i, (row, col)):
                board[row][col] = i

                if self.solve(board):
                    return True

                board[row][col] = 0

        return False

    def valid(self, board, num, pos):
        # check row
        for i in range(len(board[0])):
            if board[pos[0]][i] == num and pos[1] != i:
                return False

        # check column
        for i in range(len(board)):
            if board[i][pos[1]] == num and pos[0] != i:
                return False

        # check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if board[i][j] == num and (i,j) != pos:
                    return False

        return True

    def find_empty(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return (i, j)  # row, col
        return None

    def print_board(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - - ")
            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")
soduku = Sudoku()