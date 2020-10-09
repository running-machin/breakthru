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
        self.piececaptured= []
        self.movefunctions = {'E':self.getescortmoves,'F':self.getflagmoves}
        self.secondmove = 0
        self.breaktimer = 0 #counter
        self.silvercount = 20 #counting no.of silver escorts
        self.goldcount = 12 #counting no. of gold escorts
        self.goldwin = False
        self.silverwin = False
        self.gamedraw = False
        notation= True
    def makemove(self, move):
        self.board[move.startrow][move.startcol]='--' #moving the piece to a empty spot
        if notation:
            if move.piecemoved=='--':
                print(move.piecemoved,  move.getnotation() + "  " + str(self.secondmove), self.goldtomove)
            else:
                print(move.piecemoved, move.getnotation() + "  " + str(self.secondmove), self.goldtomove ,"captured", move.piececaptured)
        if self.board[move.endrow][move.endcol]=='--':
            self.piececaptured.append(self.board[move.endrow][move.endcol]) #capturing a piece
            
            self.secondmove = 2
        elif move.piecemoved[1] == 'F':
                self.secondmove = 2 
        else:
           
            self.secondmove +=1
        self.board[move.endrow][move.endcol] = move.piecemoved
        self.movelog.append(move)
        if self.secondmove == 2: #second move description
            self.goldtomove= not self.goldtomove
            self.breaktimer+=1
            self.secondmove = 0

    def undomove(self):
        if len(self.movelog) != 0:
            move = self.movelog.pop()
            self.board[move.startrow][move.startcol] = move.piecemoved
            self.board[move.endrow][move.endcol] = move.piececaptured
            if move.piecemoved[1]=='F': 
                self.secondmove =0            
                self.goldtomove = not self.goldtomove
            elif self.secondmove == 0:
                self.goldtomove = not self.goldtomove
                self.breaktimer -=1
                self.secondmove = 1
            elif self.secondmove:
                self.secondmove = 0    

    def getvalidmoves(self):
        return self.getallpossiblemoves()

    def getallpossiblemoves(self):
        moves=[]
        capture =[]
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                 turn = self.board[r][c][0]
                 if (turn =='g'and self.goldtomove) or (turn=='s' and not self.goldtomove ):
                    piece = self.board[r][c][1]
                    self.movefunctions[piece](r,c,moves,capture)
        return moves,capture
    
    def getescortmoves(self,r,c,moves,capture):
        if  self.secondmove == 1:
            previouspiece = self.movelog[-1] #avoid moving the same piece
            if r != previouspiece.endrow or c != previouspiece.endcol:
                self.emptyspacemoves(r,c,moves)
            
        else:
            self.emptyspacemoves(r,c,moves)
            self.capturemoves(r,c,capture)
        # directions = ((-1,0),(0,-1),(1,0),(0,1)) #up, left, down, right
        # enemy_color = 's' if self.goldtomove else 'g'
        # for d in directions:
        #     for i in range(1,11):
        #         end_row = r + d[0] * i
        #         end_col = c + d[1] * i
        #         if 0<= end_row < 11 and 0<= end_col < 11:
        #             end_piece = self.board[end_row][end_col]
        #             if end_piece == '--': # empty space valid
        #                 moves.append(Move((r,c),(end_row,end_col),self.board))
        #             elif self.board [r+1][c-1][0] == enemy_color: #enemy piece to capture
        #                 moves.append(Move((r,c),(r+1,c-1),self.board))
        #             elif self.board [r-1][c-1][0] == enemy_color: #enemy piece to capture
        #                 moves.append(Move((r,c),(r-1,c-1),self.board))
        #             elif self.board [r+1][c+1][0]== enemy_color:#enemy piece to capture
        #                 moves.append(Move((r,c),(r+1,c+1),self.board))
        #             elif self.board [r-1][c+1][0]== enemy_color:#enemy piece to capture
        #                 moves.append(Move((r,c),(r-1,c+1),self.board))
        #                 break
        #             else: break                    
        #         else: break
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
        

    def getflagmoves(self,r,c,moves,capture):
        if  self.secondmove == 0:
            self.emptyspacemoves(r,c,moves)
            self.capturemoves(r,c,moves)
        
                    
    def emptyspacemoves(self,r,c,moves):
        directions = ((-1,0),(0,-1),(1,0),(0,1)) #up, left, down, right
        
        for d in directions:
            for i in range(1,11):
                end_row = r + d[0] * i
                end_col = c + d[1] * i
                if 0<= end_row < 10 and 0<= end_col < 10:
                    end_piece = self.board[end_row][end_col]
                    if end_piece == '--':
                        moves.append(Move((r,c),(end_row,end_col),self.board))
                    else:
                        break
                else:
                    break
    
    def capturemoves(self,r,c,capture):
        enemy_color = 's' if self.goldtomove else 'g'
        if self.secondmove == 0 :
            for i in range(0,2):
                end_col = c-1 if i == 0 else c+1 #left and right
                if 0<= end_col < 11:
                    if r-1 >= 0: #up
                        if self.board[r-1][end_col][0] == enemy_color:
                            capture.append(Move((r,c),(r-1,end_col),self.board))
                    if r+1 < 11:#down
                        if self.board[r+1][end_col][0] == enemy_color:
                            capture.append(Move((r,c),(r-1,end_col),self.board))
    '''under development'''
    def gamefinal(self):
        if self.piececaptured[-1][1]=='F':
                self.silverwin = True  #if gF is captured the silver win the game 
                if move.piecemoved[1] =='F':
                    if (move.endcol == 10 or move.endcol == 0) or (move.endrow == 10 or move.endrow == 0):
                        self.goldwin = True #if the gF the is in those places gold win the game
            if self.piececaptured[-1][0] =='s':
                self.silvercount-=1
                if self.silvercount==0:
                    self.goldwin = True #if all the silver pieces(sE) are captured then the gold wins the game
            if self.piececaptured[-1] == 'gE':
                self.goldcount-=1
                if self.goldcount == 0:
                    self.silverwin = True #if all the gold escorts(gE) are captured then the silver wins the game
            if move.piecemoved[1] == 'F':
                self.secondmove = 2 
                if (move.endCol == 10 or move.endCol == 0) or (move.endRow == 0 or move.endRow == 10):
                    self.goldwin = True #if gF is in those places and its second chance then the  gold wins
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

    def getnotation(self):
        return self.getrankfile(self.startrow, self.startcol) + self.getrankfile(self.endrow, self.endcol)

    def getrankfile(self,r,c):
        return self.cols_to_files[c]+self.rows_to_ranks[r]