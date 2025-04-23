import pygame
import sys
import tiles
import player
import entity
import enemy
import render
import json
import random

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HIGHT)
full_tag = pygame.FULLSCREEN|pygame.SCALED
test_tag = pygame.SCALED|pygame.RESIZABLE 
screen = pygame.display.set_mode(SCREEN_SIZE,flags = test_tag)
clock = pygame.time.Clock()
cx=0
cy=0
tcx=0
tcy=0
pcx=1
pcy=1

with open('assets/map1.json') as json_file:
    data = json.load(json_file)
test = {}
for i in range(75):
    for j in range(50):
        test[str(i*75+j)]={
        "type":str(random.randint(-1,92)),
        "x":i,
        "y":j
    }
# print(test)
pen = render.RenderPen(screen)
tile_map = tiles.TileGrid(test)

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()
    pcx=cx
    pcy=cy
    cx += (tcx - cx)*0.3
    # print(key[pygame.K_a])
    # print(cx)
    if(key[pygame.K_a]):
        tcx -= 5

    tile_state = tile_map.get_pos(cx,cy)
    # print(pcx)
    # print(cx)
    if(round(pcx) != round(cx) or round(pcy) != round(cy) or clock.get_time()<10):
        screen.fill("#21263f")
        pen.draw("block",tile_state)
    
    print(clock.get_fps())
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
