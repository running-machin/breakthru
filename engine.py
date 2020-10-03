import numpy as np

class gamestate():
    def __init__(self):
        #the board is 11X11
        #the first character represents the colour of the piece.
        #the second character represents the type of the piece,'F'(flagship),'E'(escort),i am going to call silver fleet as silver escort
        #'--' - represents an empty space with no piece
        self.board= [['--','--','--','--','--','--','--','--','--','--','--',],
                    ['--','--','--','sE','sE','sE','sE','sE','--','--','--',],
                    ['--','--','--','--','--','--','--','--','--','--','--',],
                    ['--','sE','--','--','gE','gE','gE','--','--','sE','--',],
                    ['--','sE','--','gE','--','--','--','gE','--','sE','--',],
                    ['--','sE','--','gE','--','gF','--','gE','--','sE','--',],
                    ['--','sE','--','gE','--','--','--','gE','--','sE','--',],
                    ['--','sE','--','--','gE','gE','gE','--','--','sE','--',],
                    ['--','--','--','--','--','--','--','--','--','--','--',],
                    ['--','--','--','sE','sE','sE','sE','sE','--','--','--',],
                    ['--','--','--','--','--','--','--','--','--','--','--',]]
        self.gold_to_move = True
        self.movelog = []
    
    def make_move(self,move):
        self.board[move.start_row][move.start_col] = '--'
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.movelog.append(move) #log the move so we can undo it later
        self.gold_to_move = not self.gold_to_move

    def undo_move(self):
        if len(self.movelog) != 0:
            move = self.movelog.pop()
            self.board[move.start_row][move.start_col]= move.piece_moved
            self.board[move.end_row][move.end_col] =move.piece_captured

    def get_valid_moves(self):
        return self.get_all_possible_moves()
    
    def get_all_possible_moves(self):
        pass

class Move():
    # maps keys to values
    #key: value
    ranks_to_rows = {'1':10,'2':9,'3':8,
                    '4':7,'5':6,'6':5,'7':4,'8':3,'9':2,'10':1,'11':0}
    rows_to_ranks = {v:k for k,v in ranks_to_rows.items()}
    files_to_cols = {'a':0,'b':1,'c':2,'d':3,
                    'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10}
    cols_to_files = {v:k for k,v in files_to_cols.items()}

    def __init__(self, start_sq , end_sq, board):
        self.start_row = start_sq[0]
        self.start_col = start_sq[1]
        self.end_row = end_sq[0]
        self.end_col = end_sq[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]
    
    def get_board_notations(self):
        #can add to make this real board notation
        return self.get_rank_file(self.start_row, self.start_col) +self.get_rank_file(self.end_row, self.end_col)

    def get_rank_file(self,r,c):
        return self.cols_to_files[c]+self.rows_to_ranks[r]
