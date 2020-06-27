import pygame, sys
from pygame.locals import *
import time

#initialize global variables
XO = 'x'
winner = None
draw = False
width = 400
height = 400
white = (255, 255, 255)
line_color = (10, 10, 10)

#TicTacToe 3x3 board
TTT = [[None]*3, [None]*3, [None]*3]

#initializing pygame window
pygame.init()
fps= 30
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((width, height+100),0,32)
pygame.display.set_caption("Tic Tac Toe")

#loading the images
opening = pygame.image.load('tic tac opening.png')
x_img = pygame.image.load('x.png')
o_img = pygame.image.load('o.png')
#resizing the images
x_img = pygame.transform.scale(x_img, (80,80))
o_img = pygame.transform.scale(o_img, (80, 80))
opening = pygame.transform.scale(opening, (width, height+100))

def game_opening():
    screen.blit(opening, (0,0))
    pygame.display.update()
    time.sleep(1)
    screen.fill(white)
    #Drawing vertical lines
    pygame.draw.line(screen, line_color, (width/3,0), (width/3, height), 7)
    pygame.draw.line(screen, line_color, (width/3*2,0), (width/3*2, height), 7)
    #Drawing Horizontal lines
    pygame.draw.line(screen, line_color, (0, height/3), (width, height/3), 7)
    pygame.draw.line(screen, line_color, (0, height/3*2), (width, height/3*2), 7)
    draw_status()

def draw_status():
    global draw

    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + "You Won!"
    if draw:
        message = "Game Draw!"
    font = pygame.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))

    #copy the rendered message onto the board
    screen.fill ((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width/2, 500-50))
    screen.blit(text, text_rect)
    pygame.display.update()

#def check win
