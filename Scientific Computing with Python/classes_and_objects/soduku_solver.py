class Board:
    def __init__(self, board):
        self.board = board # refers to the board attribute of the instance of the class. It's a variable that belongs to the object created from the Board class.
    
    def __str__(self): # This method is automatically called when you use the str() function on an instance of the class or when you use print() with the object.
        upper_lines = f'\n╔═══{"╤═══"*2}{"╦═══"}{"╤═══"*2}{"╦═══"}{"╤═══"*2}╗\n'
        middle_lines = f'╟───{"┼───"*2}{"╫───"}{"┼───"*2}{"╫───"}{"┼───"*2}╢\n'
        lower_lines = f'╚═══{"╧═══"*2}{"╩═══"}{"╧═══"*2}{"╩═══"}{"╧═══"*2}╝\n'