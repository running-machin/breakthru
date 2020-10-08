import pygame as p
import engine_b 

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
    gs = engine_b.gamestate()
    validmoves = gs.getvalidmoves()
    movemade = False
    animate =False
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
                if len(playerclicks) == 2:
                    move =engine_b.Move(playerclicks[0],playerclicks[1],gs.board)    
                    print(move.getchessnotation())
                    if move in validmoves :
                        gs.makemove(move)
                        movemade = True
                        animate = True
                        sqselected =()
                        playerclicks =[]
                    elif move in capturemoves:
                        gs.makemove(move)
                        movemade = True
                        animate = True
                        sqselected = ()
                        playerclicks = []
                    else:
                        playerclicks = [sqselected]                    
                    
            elif e.type == p.KEYDOWN:
                if e.key ==p.K_z:
                     gs.undomove()
                     movemade = True
                     animate = False
                if e.key == p.K_r:
                    gs= engine_b.gamestate()
                    validmoves,capturemoves = gs.getvalidmoves()
                    sqselected =()
                    playerclicks= []
                    movemade = False
                    animate = False

       
        if movemade:
            if animate:
                animatemoves(gs.movelog[-1],screen,gs.board,clock)
            validmoves,capturemoves = gs.getvalidmoves()
            movemade = False
        drawgamestate(screen, gs,validmoves,capturemoves,sqselected)
        clock.tick(MAX_FPS)
        p.display.flip()
        if gs.breaktimer==0:
            p.time.wait(1500)
            gs.breaktimer=1


def drawgamestate(screen, gs,validmoves,capturemoves,sqselected):
    drawboard(screen)
    highlightsquares(screen,gs,validmoves,sqselected,p.Color('yellow'))
    highlightsquares(screen,gs,capturemoves,sqselected,p.Color('red'))
    drawpieces(screen, gs.board)

def highlightsquares(screen,gs,moves,sqselected,color):
    if sqselected !=():
        r,c,= sqselected
        if gs.board[r][c][0]== ('g' if gs.goldtomove else 's'):
            s = p.Surface((SQ_SIZE,SQ_SIZE))
            s.set_alpha(100)
            s.fill(p.Color('blue'))
            screen.blit(s,(c*SQ_SIZE, r*SQ_SIZE))
            s.fill(color)
            for move in moves :
                if move.startrow == r and move.startcol == c:
                    screen.blit(s,(SQ_SIZE*move.endcol,move.endrow*SQ_SIZE))

def drawboard(screen):
    global colors
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

def animatemoves(move,screen,board,clock):
    global colors
    dR = move.endrow - move.startrow
    dC = move.endcol - move.startcol
    framespersquare = 10
    framescount = (abs(dR)+abs(dC))*framespersquare
    for frame in range(framescount+1):
        r,c = (move.startrow+dR*frame/framescount,move.startcol+dC*frame/framescount)
        drawboard(screen)
        drawpieces(screen, board)
        endsquare = p.Rect(move.endcol*SQ_SIZE,move.endrow*SQ_SIZE,SQ_SIZE,SQ_SIZE)
        p.draw.rect(screen,colors[0],endsquare)
        if move.piececaptured != '--':
            screen.blit(IMAGES[move.piececaptured],endsquare)
        screen.blit(IMAGES[move.piecemoved],p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))
        p.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()