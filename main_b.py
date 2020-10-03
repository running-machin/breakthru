import pygame as p
import engine_b as chess_engine

WIDTH= HEIGHT = 517
DIMENSION = 11
SQ_SIZE = HEIGHT// DIMENSION
MAX_FPS = 15
IMAGES= {}

def loadimages():
    pieces  = ['sE','gE','gF']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load('images/'+piece+'.png'),(SQ_SIZE,SQ_SIZE))

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = chess_engine.gamestate()
    validmoves = gs.getvalidmoves()
    movemade = False
    loadimages()
    running = True
    sqselected =()
    playerclicks= []
    
    while running:
        for e in p.event.get():
            if e.type ==p.QUIT:
                running =False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0]//SQ_SIZE
                row = location[1]// SQ_SIZE
                if sqselected ==(row,col ):
                    sqselected= ()
                    playerclicks= []
                else:
                    sqselected= (row,col)
                    playerclicks.append(sqselected)
                if len(playerclicks)== 2:
                    move =chess_engine.Move(playerclicks[0],playerclicks[1],gs.board)    
                    print(move.getchessnotation())
                    if move in validmoves:
                        gs.makemove(move)
                        movemade = True
                        sqselected=()
                        playerclicks= []
                    else:
                        playerclicks= [sqselected]    
            elif e.type == p.KEYDOWN:
                if e.key ==p.K_z:
                     gs.undomove()
                     movemade = True
        if movemade:
            validmoves = gs.getvalidmoves()
            movemade = False
        drawgamestate(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

def drawgamestate(screen, gs):
    drawboard(screen)
    drawpieces(screen, gs.board)

def drawboard(screen):
    colors = [p.Color('white'), p.Color('gray')]    
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            #color = colors[(r+c)%2]
            p.draw.rect(screen, colors[0], p.Rect(c*SQ_SIZE,r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            p.draw.rect(screen, colors[1], p.Rect(c*SQ_SIZE,r*SQ_SIZE, SQ_SIZE, SQ_SIZE),1)
    for r in range(DIMENSION-6):
        for c in range(DIMENSION-6):      
            p.draw.rect(screen, p.Color('red'),p.Rect((c+3)*SQ_SIZE,(r+3)*SQ_SIZE, SQ_SIZE, SQ_SIZE),1)


def drawpieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != '--':
                screen.blit(IMAGES[piece],p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))



if __name__ == '__main__':
    main()