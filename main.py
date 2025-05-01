import pygame
import sys
import tiles
import player
import entity
import enemy
import render
import json
import random
from os import listdir
from os.path import isfile, join

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HIGHT)
SCREEN_CENTER = (SCREEN_WIDTH/2,SCREEN_HIGHT/2)
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

player_frames = [pygame.transform.scale(pygame.image.load(join("./assets/entitys/player/idle/",f)),(32,64)) for f in listdir("./assets/entitys/player/idle") if isfile(join("./assets/entitys/player/idle",f))]
print(player_frames)

player = entity.AnimatedEntity(SCREEN_WIDTH/2-16, SCREEN_WIDTH/2-32, player_frames,pygame.rect.Rect(SCREEN_WIDTH/2, SCREEN_WIDTH/2,32,64) ,4)

with open('assets/map1.json') as json_file:
    data = json.load(json_file)
# test = {}
# for i in range(75):
#     for j in range(50):
#         test[str(i*75+j)]={
#         "type":str(random.randint(-1,92)),
#         "x":i,
#         "y":j
#     }
# print(test)
pen = render.RenderPen(screen)
tile_map = tiles.TileGrid(data)
a_fake = tiles.FakeGrid()

while(True):
    delta = 60/(clock.get_fps()+0.000000000000000000000000000000000000000001)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()
    pcx=cx
    pcy=cy
    cx += (tcx - cx)*0.3*delta
    cy += (tcy - cy)*0.3*delta
    # print(key[pygame.K_a])
    # print(cx)
    if(key[pygame.K_a]):
        tcx -= 5
    if(key[pygame.K_d]):
        tcx += 5
    if(key[pygame.K_s]):
        tcy -= 5
    if(key[pygame.K_w]):
        tcy += 5
    # print(pcx)
    # print(cx)
    if(round(pcx) != round(cx) or round(pcy) != round(cy) or clock.get_time()<10):
        tile_state = tile_map.get_pos(cx,cy)
        a_fake.shift(cx,cy)
        screen.fill("#21263f")
        pen.draw("block",tile_state)
    
    player.update(SCREEN_CENTER[0]-24,SCREEN_CENTER[1]-48,screen)

    # print(clock.get_fps())
    pygame.display.flip()
    pygame.display.update()
    clock.tick()
