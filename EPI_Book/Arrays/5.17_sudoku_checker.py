'''
Checks if a given incomplete sudoku board is valid or not
'''
def valid_sudoku(self, board):
    seen = []
    for i, row in enumerate(board):
        for j, c in enumerate(row):
            if c != '.':
                seen += [(i,c), (c,j), (i//3,j//3, c)]
    
    return len(seen) == len(set(seen))