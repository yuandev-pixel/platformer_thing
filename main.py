import pygame
import sys
import tiles
import player
import entity
import enemy
import render
import json

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE,flags = pygame.RESIZABLE|pygame.SCALED)
cx=0
cy=0

with open('assets/map1.json') as json_file:
    data = json.load(json_file)
test = {}
for i in range(75):
    for j in range(50):
        test[str(i*75+j)]={
        "type":"25",
        "x":i,
        "y":j
    }
print(test)
pen = render.RenderPen(screen)
tile_map = tiles.TileGrid(test)

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("#ffffff")

    tile_state = tile_map.get_pos(cx,cy)
    pen.draw("block",tile_state)
    
    
    pygame.display.flip()
    pygame.display.update()
