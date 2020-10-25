import random
import engine_b
from copy import deepcopy
global_depth=4
eng = engine_b.gamestate
next_s=deepcopy(eng)

def __init__(self):
        self.global_depth=4
        self.best_move=""
#move = eng.move

def select_minmax_move(self,gs):
    validmoves,capturemoves = gs.getvalidmoves()
    #minmax/alphabeta
    aimove,minmax_values= minmax(next_s,self.global_depth,100000,-100000,"")
    
    return aimove
def selectmove(gs):
    validmoves,capturemoves = gs.getvalidmoves()
    #minmax/alphabeta
    aimove= alpha_beta(next_s,global_depth,100000,-100000,"")
    """random AI"""
    # if len(capturemoves) !=0 :
    #     aimove = random.choice(capturemoves)
    # else:
    #     aimove = random.choice(validmoves)
    
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

def minmax(self,state,depth,moves,scores,is_max):
        self.bestmove=""
        validmoves,capturemoves = next_s.getvalidmoves()
        moves =  capturemoves+validmoves
        if (depth==0 and len(moves)==0):
            return evaluation_function(moves)
        best_value = 100000 if is_max else -100000
        for move in moves:
            value = (evaluation_function(moves))
            moves, value =self.minmax(depth-1,next_s,not is_max)

            if is_max and best_value< value:
                best_value=value
                bestmove = move
            elif (not is_max) and best_value>value:
                best_value=value
                bestmove = move
        return bestmove, best_value

        
       
def alpha_beta(gs,depth,beta,alpha,list):
    
    best_move=""
    validmoves,capturemoves = next_s.getvalidmoves()
    moves =  capturemoves+validmoves
    if (depth==0 and len(moves)==0):
        val = evaluation_function(moves)   
    for move in moves:
        next_s.makemove(move)
        value = alpha_beta(gs,depth-1,beta,alpha,moves)
        if value<=beta:
            beta=value
            if (depth==global_depth): break 
        else:
            if value>alpha:
                if (depth==global_depth):
                    best_move=move  
        if alpha>=beta:
                bestvalue=value
                best_move = move
        else:
            bestvalue = beta
    return best_move


# def next_s(move,gs):
#     nextgs=deepcopy(gs)
    

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

    
    
    


    
        