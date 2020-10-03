class gamestate():
    def __init__(self):
        self.board= [
                    ['--','--','--','--','--','--','--','--','--','--','--',],
                    ['--','--','--','sE','sE','sE','sE','sE','--','--','--',],
                    ['--','--','--','--','--','--','--','--','--','--','--',],
                    ['--','sE','--','--','gE','gE','gE','--','--','sE','--',],
                    ['--','sE','--','gE','--','--','--','gE','--','sE','--',],
                    ['--','sE','--','gE','--','gF','--','gE','--','sE','--',],
                    ['--','sE','--','gE','--','--','--','gE','--','sE','--',],
                    ['--','sE','--','--','gE','gE','gE','--','--','sE','--',],
                    ['--','--','--','--','--','--','--','--','--','--','--',],
                    ['--','--','--','sE','sE','sE','sE','sE','--','--','--',],
                    ['--','--','--','--','--','--','--','--','--','--','--',]
                    ]
        self.goldtomove =True
        self.movelog = []
        self.movefunctions = {'E':self.getescortmoves,'F':self.getflagmoves}
    def makemove(self, move):
        self.board[move.startrow][move.startcol]='--'
        self.board[move.endrow][move.endcol] = move.piecemoved
        self.movelog.append(move)
        self.goldtomove= not self.goldtomove

    def undomove(self):
        if len(self.movelog) != 0:
            move = self.movelog.pop()
            self.board[move.startrow][move.startcol] = move.piecemoved
            self.board[move.endrow][move.endcol] = move.piececaptured
            self.goldtomove = not self.goldtomove

    def getvalidmoves(self):
        return self.getallpossiblemoves()

    def getallpossiblemoves(self):
        moves=[]
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                 turn = self.board[r][c][0]
                 if (turn =='g'and self.goldtomove) or (turn=='s' and not self.goldtomove ):
                    piece = self.board[r][c][1]
                    self.movefunctions[piece](r,c,moves)
        return moves
    def getescortmoves(self,r,c,moves):
                
        directions = ((-1,0),(0,-1),(1,0),(0,1)) #up, left, down, right
        enemy_color = 's' if self.goldtomove else 'g'
        for d in directions:
            for i in range(1,11):
                end_row = r + d[0] * i
                end_col = c + d[1] * i
                if 0<= end_row < 11 and 0<= end_col < 11:
                    end_piece = self.board[end_row][end_col]
                    if end_piece == '--': # empty space valid
                        moves.append(Move((r,c),(end_row,end_col),self.board))
                    elif self.board [r+1][c-1][0] == enemy_color: #enemy piece to capture
                        moves.append(Move((r,c),(r+1,c-1),self.board))
                    elif self.board [r-1][c-1][0] == enemy_color: #enemy piece to capture
                        moves.append(Move((r,c),(r-1,c-1),self.board))
                    elif self.board [r+1][c+1][0]== enemy_color:#enemy piece to capture
                        moves.append(Move((r,c),(r+1,c+1),self.board))
                    elif self.board [r-1][c+1][0]== enemy_color:#enemy piece to capture
                        moves.append(Move((r,c),(r-1,c+1),self.board))
                        break
                    else: break
                
                    
                else: break
        # if c-1 >= 0 : #enemy capture to the left
        #     if self.board [r+1][c-1][0] == enemy_color: #enemy piece to capture
        #         moves.append(Move((r,c),(r+1,c-1),self.board))
        #     if self.board [r-1][c-1][0] == enemy_color: #enemy piece to capture
        #         moves.append(Move((r,c),(r-1,c-1),self.board))
        # if c+1 <= 10 : #enemy capture to the right
        #     if self.board [r+1][c+1][0]== enemy_color:#enemy piece to capture
        #         moves.append(Move((r,c),(r+1,c+1),self.board))
        #     if self.board [r-1][c+1][0]== enemy_color:#enemy piece to capture
        #         moves.append(Move((r,c),(r-1,c+1),self.board))
        

    def getflagmoves(self,r,c,moves):
        directions = ((-1,0),(0,-1),(1,0),(0,1)) #up, left, down, right
        enemy_color = 's' if self.goldtomove else 'g'
        for d in directions:
            for i in range(1,11):
                end_row = r + d[0] * i
                end_col = c + d[1] * i
                if 0<= end_row < 11 and 0<= end_col < 11:
                    end_piece = self.board[end_row][end_col]
                    if end_piece == '--': # empty space valid
                        moves.append(Move((r,c),(end_row,end_col),self.board))
                        
                if c-1 >= 0 : #enemy capture to the left
                    if self.board [r+1][c-1][0] == enemy_color: #enemy piece to capture
                        moves.append(Move((r,c),(r+1,c-1),self.board))
                    if self.board [r-1][c-1][0] == enemy_color: #enemy piece to capture
                        moves.append(Move((r,c),(r-1,c-1),self.board))
                if c+1 <= 10 : #enemy capture to the right
                    if self.board [r+1][c+1][0]== enemy_color:#enemy piece to capture
                        moves.append(Move((r,c),(r+1,c+1),self.board))
                    if self.board [r-1][c+1][0]== enemy_color:#enemy piece to capture
                        moves.append(Move((r,c),(r-1,c+1),self.board))
                else:
                    break

class Move():
    ranks_to_rows = {'1':10,'2':9,'3':8,
                    '4':7,'5':6,'6':5,'7':4,'8':3,'9':2,'10':1,'11':0}
    rows_to_ranks = {v:k for k,v in ranks_to_rows.items()}
    files_to_cols = {'a':0,'b':1,'c':2,'d':3,
                    'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10}
    cols_to_files = {v:k for k,v in files_to_cols.items()}

    def __init__(self, startsq, endsq,board):
        self.startrow = startsq[0]
        self.startcol = startsq[1]
        self.endrow = endsq[0]
        self.endcol = endsq[1]
        self.piecemoved = board[self.startrow][self.startcol]
        self.piececaptured = board[self.endrow][self.endcol]
        self.moveid = self.startrow*100000+self.startcol*10000+self.endrow*100+self.endcol*1
        

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveid == other.moveid

    def getchessnotation(self):
        return self.getrankfile(self.startrow, self.startcol) + self.getrankfile(self.endrow, self.endcol)

    def getrankfile(self,r,c):
        return self.cols_to_files[c]+self.rows_to_ranks[r]