class Board:
    def __init__(self, board):
        self.board = board # refers to the board attribute of the instance of the class. It's a variable that belongs to the object created from the Board class.
    
    def __str__(self): # This method is automatically called when you use the str() function on an instance of the class or when you use print() with the object.
        upper_lines = f'\n╔═══{"╤═══"*2}{"╦═══"}{"╤═══"*2}{"╦═══"}{"╤═══"*2}╗\n'
        middle_lines = f'╟───{"┼───"*2}{"╫───"}{"┼───"*2}{"╫───"}{"┼───"*2}╢\n'
        lower_lines = f'╚═══{"╧═══"*2}{"╩═══"}{"╧═══"*2}{"╩═══"}{"╧═══"*2}╝\n'
        board_string = upper_lines

        for line, index in enumerate(self.board):
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
