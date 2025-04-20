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
screen = pygame.display.set_mode(SCREEN_SIZE)
cx=0
cy=0

with open('assets/map1.json') as json_file:
    data = json.load(json_file)
print(data)
#pen = render.RenderPen()
tile_map = tiles.TileGrid(data)

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tile_state = tile_map.get_pos(cx,cy)
    # pen.draw()

    screen.fill("#ffffff")
    pygame.display.flip()
