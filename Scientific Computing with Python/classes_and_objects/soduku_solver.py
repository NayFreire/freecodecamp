class Board:
    def __init__(self, board):
        self.board = board # refers to the board attribute of the instance of the class. It's a variable that belongs to the object created from the Board class.
    
    def __str__(self): # This method is automatically called when you use the str() function on an instance of the class or when you use print() with the object.
        upper_lines = f'\n╔═══{"╤═══"*2}{"╦═══"}{"╤═══"*2}{"╦═══"}{"╤═══"*2}╗\n'
        middle_lines = f'╟───{"┼───"*2}{"╫───"}{"┼───"*2}{"╫───"}{"┼───"*2}╢\n'
        lower_lines = f'╚═══{"╧═══"*2}{"╩═══"}{"╧═══"*2}{"╩═══"}{"╧═══"*2}╝\n'
        board_string = upper_lines

        for index, line in enumerate(self.board):
            row_list = []
            for square_no, part in enumerate([line[:3], line[3:6], line[6:]], start=1): #If the first line of sudoku is:
            # 1 | X | 5 | 3 | X | 4 | 8 | X | X 
            # Means that 1, X and 5 are from the first square, 3, X and 4 are from the second square and 8, X and X are from the third square. Instead of starting at 0, the enumerate starts at 1
                row_square = "|".join(str(item) for item in part)
                row_list.extend(row_square) # extends add multiples elements to the end of the list. For more info "extends_and_append.py"

                if square_no != 3: #if the square in the board isn't the last one...
                    row_list.append('║') #... put this character
            row = f'║ {" ".join(row_list)} ║\n'
            row_empty = row.replace('0', ' ') #replacing the 0 used for empty sparec with ' '.

            board_string += row_empty

            if index < 8: #Verifying if we are at the last row of the board
                if index % 3 == 2: # if we are at the last row of the 3x3 squares...
                    board_string += f'╠═══{"╪═══"*2}{"╬═══"}{"╪═══"*2}{"╬═══"}{"╪═══"*2}╣\n' # ... use this line for aesthetic purposes
                else:
                    board_string += middle_lines
            else: # If this is the last line oin the board...
                board_string += lower_lines #... use the lower_lines
        return board_string
    
    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None
    
    def valid_in_row(self, row, num):
        return num not in self.board[row] #Is this number valid to be put in this row?
    
    def valid_in_col(self, col, num):
        return all(
            self.board[row][col] != num
            for row in range(9)
        ) #Also can be written like all(self.board[row[col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        row_start = (row // 3) * 3 # Getting th index of the row that starts the square in question
        col_start = (col // 3) * 3 # Getting th index of the column that starts the square in question

        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num: # If the number in question is already inside the square...
                    return False #... return False, meaning it cannot go there
        return True #If the number is not in the square already, return True, meaning it can go there
    
    def is_valid(self, empty, num):
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all(
            [valid_in_row, valid_in_col, valid_in_square]
        )
    
    def solver(self):
        if (next_empty := self.find_empty_cell()) is None: # If there are no more empty cells...
            return True #... the sudoku has been solved
        else: #If there are still empty cells...
            for guess in range(1, 10): #Iterate from 1 to 9 (the second value in range is non-inclusive)
                if self.is_valid(next_empty, guess): # If a number is valid for this empty cell
                    row, col = next_empty #get the row and column...
                    self.board[row][col] = guess #... and assign this guess to the empty cell
                    
                    if self.solver(): #If the recursive call returns true...
                        return True #... the soduko is solved
                    self.board[row][col] = 0 # #If the recursive call returns false, the guess made the sudoku unsolvable, so the cell needs to go back to 0
            return False #Means that none of the guesses lead to a solution
        
def solve_sudoku(board):
    gameboard = Board(board)
    print(gameboard)
    print(f'\nPuzzle to solve:\n{gameboard}')

    if gameboard.solver():
        print('\nSolved puzzle:')
        print(gameboard)
    else:
        print('\nThe provided puzzle is unsolvable.')

    return gameboard

puzzle = [
    [0, 0, 2, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 7, 6, 2],
    [4, 3, 0, 0, 0, 0, 8, 0, 0],
    [0, 5, 0, 0, 3, 0, 0, 9, 0],
    [0, 4, 0, 0, 0, 0, 0, 2, 6],
    [0, 0, 0, 4, 6, 7, 0, 0, 0],
    [0, 8, 6, 7, 0, 4, 0, 0, 0],
    [0, 0, 0, 5, 1, 9, 0, 0, 8],
    [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

solve_sudoku(puzzle)