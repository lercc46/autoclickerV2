import sys
import pygame as pg
from pynput.mouse import Controller, Button

print("hello, welcome to Luke's autoclicker :)")

TOGGLE = input("choose a key to toggle: ").lower()
QUIT = input("choose a key to quit: ").lower()
speed = int(input("choose a speed (clicks per second): "))
SPEED = 1 / speed

print("have fun :)")


clicking = False
run = True
mouse = Controller()

def toggle():
    global clicking
    clicking = not clicking

def quit():
    global run
    run = False
    sys.exit()


pg.init()

clock = pg.time.Clock()
while run:
    clock.tick(SPEED)

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            print("keydown")
            if event.unicode == TOGGLE:
                print("toggling")
                toggle()
                
            if event.unicode == QUIT:
                print("quitting")
                quit()

    if clicking:
        mouse.click(Button.left, 1)