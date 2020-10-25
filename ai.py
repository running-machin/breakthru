import random
import engine_b
from copy import deepcopy
global_depth=4
eng = engine_b.gamestate
#move = eng.move
def selectmove( gs):
    validmoves,capturemoves = gs.getvalidmoves()
    if len(capturemoves) !=0 :
        aimove = random.choice(capturemoves)
    else:
        aimove = random.choice(validmoves)
    
    # best_score = -1000
    # temp_board= gs.board.copy()
    # for moves in validmoves:
    #     gs.makemove(moves)
    #     score = self.evaluation_function()
    #     if score > best_score:
    #         best_score = score
    #         aimove = moves
    print (aimove)
    return aimove

#totally wont work!!        
def alpha_beta(self,state,depth,beta,alpha):
    best_move=""
    validmoves,capturemoves = next_s.getvalidmoves()
    listx =  capturemoves+validmoves
    if (depth==0 and len(listx)==0):
        val = evaluation_function(listx)   #move+score*(player*2-1)
    for i in listx:
        next_s.makemove(i)
        value = alpha_beta(depth-1,beta,alpha,list,player)
        if value<=beta:
            beta=value
            if (depth==global_depth):bestmove=i  #move is not correct
        else:
            if value>alpha:
                if (depth==global_depth):bestmove=i  #the whole thing might not be correct
        if alpha>=beta:
                bestvalue=value
                bestmove = bestmove
        else:
            bestvalue = beta
    del validmoves,capturemoves


def next_s(self,move,gs):
    nextgs=deepcopy(gs)
    nextgs.makemove(move)
    return nextgs
   

def score_position(self,gs):
    return 0
    



def evaluation_function(self):
#     score = 0
#     if move.piececaptured[1] == 'E':
#         score = 100
#     if move.piececaptured[1] == 'F':
#         score=1000
#     #in check score should be -500
#     if move.piecemoved[1] == 'F':
#         if (move.endcol == 10 or move.endcol == 0) or (move.endrow == 10 or move.endrow == 0):
#             score = 1000
    return 0    
class minmax:
    pass