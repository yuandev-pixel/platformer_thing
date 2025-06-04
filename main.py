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
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HIGHT)
SCREEN_CENTER = (SCREEN_WIDTH / 2, SCREEN_HIGHT / 2)
full_tag = pygame.FULLSCREEN | pygame.SCALED | pygame.DOUBLEBUF | pygame.HWSURFACE
test_tag = pygame.SCALED | pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE
screen = pygame.display.set_mode(SCREEN_SIZE, flags=test_tag, vsync = 1)
clock = pygame.time.Clock()
camera_x = 0
camera_y = 0
target_camera_x = 0
target_camera_y = 0
previous_camera_x = 1
previous_camera_y = 1

player_idle_frames = [
    pygame.transform.scale(
        pygame.image.load(join("./assets/entitys/player/idle/", f)), (32, 64)
    )
    for f in listdir("./assets/entitys/player/idle")
    if isfile(join("./assets/entitys/player/idle", f))
]

player_idle = entity.AnimatedEntity(
    round(SCREEN_WIDTH / 2) - 16,
    round(SCREEN_WIDTH / 2) - 32,
    player_idle_frames,
    pygame.rect.Rect(SCREEN_WIDTH / 2, SCREEN_WIDTH / 2, 32, 64),
    4,
)
dirty_player_idle = player_idle

select_tile = pygame.image.load("./assets/tiles/select.png")
select_tile = pygame.transform.scale(select_tile,(16,16)).convert_alpha()
dirty_select_tile = select_tile

preview_tile = []

with open("assets/map1.json") as json_file:
    data = json.load(json_file)

test = {}
for i in range(75):
    for j in range(50):
        test[str(i*75+j)]={
        "type":str(-2),
        "x":i,
        "y":j
    }

pen = render.RenderPen(screen)
tile_map = tiles.TileGrid(test)
a_fake = tiles.FakeGrid()

while True:
    #清空屏幕

    screen.fill("#21263f")

    #逻辑部分

    #帧率改变逻辑
    delta = round(60 / (clock.get_fps() + 0.000000000000000000000000000000000000000001), 2)

    #退出游戏
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #移动逻辑
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        camera_x -= round(0.5 * delta)
    if key[pygame.K_d]:
        camera_x += round(0.5 * delta)
    if key[pygame.K_s]:
        camera_y += round(0.5 * delta)
    if key[pygame.K_w]:
        camera_y -= round(0.5 * delta)

    #更新角色
    player_idle.update(round(SCREEN_CENTER[0]) - 24, round(SCREEN_CENTER[1]) - 48)

    #格子逻辑
    tile_state = tile_map.get_pos(camera_x, camera_y)

    #选择格子
    mouse_pos = pygame.mouse.get_pos()
    a_fake.shift(-camera_x, -camera_y)
    mouse_tile_pos = mouse_pos[0]//16*16, mouse_pos[1]//16*16
    real_mouse_tile_pos = mouse_tile_pos[0]/16 + camera_x, mouse_tile_pos[1]/16 + camera_y
    print(real_mouse_tile_pos)
    print(camera_x,camera_y)

    #做关卡
    if  pygame.mouse.get_pressed()[0]:
        test[str(real_mouse_tile_pos[0]*75+real_mouse_tile_pos[1])]={
        "type":str(2),
        "x":real_mouse_tile_pos[0],
        "y":real_mouse_tile_pos[1]
        }
        tile_map.reload(test)

    #绘制部分

    #绘制格子
    pen.draw("block", tile_state)

    #绘制选择
    screen.blit(select_tile,mouse_tile_pos)

    #绘制玩家
    player_idle.draw(screen)

    #更新画面

    pygame.display.flip()
    pygame.display.update()
    clock.tick(120)
