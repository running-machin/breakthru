import pygame as pg
import numpy as np
import engine

WIDTH = HEIGHT = 517
DIMENISIONS = 11 #dimensions of the board are 8X8
SQ_SIZE = HEIGHT//DIMENISIONS
MAX_FPS = 15 #for animations
IMAGES = {}

def load_images():
   pieces = ['sE','gE','gF']
   for piece in pieces:
        IMAGES[piece] = pg.transform.scale(pg.image.load('images/'+piece+'.png'),(SQ_SIZE,SQ_SIZE))


def main():
   pg.init()
   screen = pg.display.set_mode((WIDTH,HEIGHT))
   clock = pg.time.Clock()
   screen.fill(pg.Color('white'))
   gs = engine.gamestate()
   valid_moves = gs.get_valid_moves()
   move_made = False
   load_images()
   running = True
   sq_selected = ()
   playerclicks = []
   while running:
      for e in pg.event.get():
         if e.type == pg.QUIT:
            running = False
         #mouse handler
         elif e.type == pg.MOUSEBUTTONDOWN:
            location = pg.mouse.get_pos() #(x,y ) location of mouse
            col = location[0]//SQ_SIZE
            row = location[1]//SQ_SIZE
            if sq_selected == (row, col):
               sq_selected = ()
               playerclicks = []
            else:
               sq_selected = (row, col)
               playerclicks.append(sq_selected)
            if len(playerclicks) == 2:
               move = engine.Move(playerclicks[0],playerclicks[1],gs.board)
               print(move.get_board_notations())
               gs.make_move(move)
               sq_selected =() #reset the clicks
               playerclicks =[]
            else:
               playerclicks = [sq_selected]
         #key handler
         elif  e.type == pg.KEYDOWN:
            if e.key == pg.K_z:
               gs.undo_move()
               move_made = True
      if move_made: 
         valid_moves = gs.get_valid_moves()
         move_made =False
            
      draw_game_state(screen, gs)
      clock.tick(MAX_FPS)
      pg.display.flip()

def draw_game_state(screen,gs):
   draw_board(screen)
   draw_pieces(screen, gs.board)


def draw_board(screen):
 #draw the squares on the board
   # img =pg.image.load('F:/python project/Breakthru/images/breakthru_board.jpeg')
   # img2 =pg.transform.scale(img,(DIMENISIONS*SQ_SIZE,DIMENISIONS*SQ_SIZE))
   # screen.blit(img2)
   for r in range(DIMENISIONS):
      for c in range(DIMENISIONS):
         pg.draw.rect(screen,pg.Color('dark grey'), pg.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE), 1)
   #Draw the flagship boundary
   # for r in range (DIMENISIONS-6):
   #    for c in range(DIMENISIONS-6):
   #       pg.draw.rect(screen,pg.Color('gray'), pg.Rect((c+3)*SQ_SIZE, (r+3)*SQ_SIZE, SQ_SIZE, SQ_SIZE) )
   #       pg.draw.rect(screen,pg.Color('red'), pg.Rect((c+3)*SQ_SIZE, (r+3)*SQ_SIZE, SQ_SIZE, SQ_SIZE), 1)
   
def draw_pieces(screen, board):
    for r in range(DIMENISIONS):
       for c in range (DIMENISIONS):
          piece = board[r][c]
          if piece != '--':
             screen.blit(IMAGES[piece],pg.Rect(c*SQ_SIZE, r*SQ_SIZE,SQ_SIZE, SQ_SIZE ))

if __name__ == '__main__':
   main()