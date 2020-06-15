import time

import pygame as pg
import sys
from pygame.locals import *

import minimax


def game_start():
    screen.blit(load_png,(0,0))
    pg.display.update()
    time.sleep(1)
    screen.fill(white)

    pg.draw.line(screen,line_color,(width//3,0),(width//3, height),7)
    pg.draw.line(screen,line_color,(width//3*2,0),(width//3*2, height),7)
    # Drawing horizontal lines
    pg.draw.line(screen,line_color,(0,height//3),(width, height//3),7)
    pg.draw.line(screen,line_color,(0,height//3*2),(width, height//3*2),7)
    
    status()


def status():

    global draw

    print("In Status")
    print(winner)

    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = "X won!" if XO == "o" else "O won!"
    
    if draw:
        message = 'Game Draw !'

    font = pg.font.Font(None, 30)
    text = font.render(message ,1 ,(255,255,255))

    screen.fill((0,0,0) , (0,400,500,100))
    text_rect = text.get_rect(center = (width // 2 , 500-50))
    screen.blit(text,text_rect)
    pg.display.update()

def check_win():
    global draw, winner, brd 

    # print(minimax.current_board_score(brd,3,3))

    print("In Check Win")
    print(brd)

    for row in range (0,3):
        if ((brd [row][0] == brd[row][1] == brd[row][2]) and(brd [row][0] is not None)):
            winner = brd[row][0]
            pg.draw.line(screen, (250,0,0), (0, (row + 1)*height//3 -height//6),(width, (row + 1)*height//3 - height//6 ), 4)
            break

    for col in range (0, 3):
        if (brd[0][col] == brd[1][col] == brd[2][col]) and (brd[0][col] is not None):
            winner = brd[0][col]
            pg.draw.line (screen, (250,0,0),((col + 1)* width//3 - width//6, 0),((col + 1)* width//3 - width//6, height), 4)
            break

    if (brd[0][0] == brd[1][1] == brd[2][2]) and (brd[0][0] is not None):
        winner = brd[0][0]
        pg.draw.line (screen, (250,70,70), (50, 50), (350, 350), 4)

    if (brd[0][2] == brd[1][1] == brd[2][0]) and (brd[0][2] is not None):
        winner = brd[0][2]
        pg.draw.line (screen, (250,70,70), (350, 50), (50, 350), 4)

    if(all([all(row) for row in brd]) and winner is None ):
        draw = True

    status()

def drawXO(row,col):

    global XO,brd

    if row==1:
        posy = 30
    if row==2:
        posy = width//3 + 30
    if row==3:
        posy = width//3*2 + 30
    if col==1:
        posx = 30
    if col==2:
        posx = height//3 + 30
    if col==3:
        posx = height//3*2 + 30

    brd[row-1][col-1] = XO
    if XO == 'x':
        screen.blit(x,(posx,posy))
        XO = 'o'
    else:
        screen.blit(o,(posx,posy))
        XO = 'x'

    pg.display.update()

def userClick():
    x,y = pg.mouse.get_pos()
    #get column of mouse click (1-3)
    if(x < width//3):
        col = 1
    elif (x < width//3*2):
        col = 2
    elif(x < width):
        col = 3
    else:
        col = None
    #get row of mouse click (1-3)
    if(y < height//3):
        row = 1
    elif (y < height//3*2):
        row = 2
    elif(y<height):
        row = 3
    else:
        row = None
    if (row and col and brd[row - 1][col - 1] is None):
        drawXO(row,col)

def nextMove(): 

    global brd,XO

    r , c = minimax.bestMove(brd,'o')
    print("AI's move : ",(r,c))
    drawXO(r+1,c+1)
    check_win()

def reset():

    global brd, winner, XO, draw

    time.sleep(3)
    XO = 'x'
    draw = False
    game_start()
    winner = None
    brd = [[None , None , None] for i in range(3)] 

global brd,draw,winner,XO,screen,x,o

XO = 'x'
winner = None
draw = False
width , height = 400,400
white = (255,255,255)
line_color = (10,10,10)

brd = [[None , None , None] for i in range(3)]

pg.init()
clk = pg.time.Clock()
screen = pg.display.set_mode((width , height + 100) , 0, 32) # set_mode(resolution=(0,0), flags=0, depth=0) 
pg.display.set_caption("Tic Tac Toe")

load_png = pg.image.load('Tic-tac-toe.png')
x = pg.image.load('x.png')
o = pg.image.load('o.png')

x = pg.transform.scale(x,(80,80))
o = pg.transform.scale(o,(80,80))
load_png = pg.transform.scale(load_png,(width,height))


game_start()

while(1):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type is MOUSEBUTTONDOWN:
            userClick()
            nextMove()
            if (winner or draw):
                reset()
            print(brd)

        pg.display.update()
        clk.tick(30)
