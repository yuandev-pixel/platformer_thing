import pygame
import sys
import tiles
import player
import entity
import enemy
import render
import json
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
cx = 0
cy = 0
tcx = 0
tcy = 0
pcx = 1
pcy = 1

player_idle_frames = [
    pygame.transform.scale(
        pygame.image.load(join("./assets/entitys/player/idle/", f)), (32, 64)
    )
    for f in listdir("./assets/entitys/player/idle")
    if isfile(join("./assets/entitys/player/idle", f))
]

player_idle = entity.AnimatedEntity(
    SCREEN_WIDTH / 2 - 16,
    SCREEN_WIDTH / 2 - 32,
    player_idle_frames,
    pygame.rect.Rect(SCREEN_WIDTH / 2, SCREEN_WIDTH / 2, 32, 64),
    4,
)
dirty_player_idle = player_idle

select_tile = pygame.image.load("./assets/tiles/select.png")
select_tile = pygame.transform.scale(select_tile,(16,16)).convert_alpha()
dirty_select_tile = select_tile

with open("assets/map1.json") as json_file:
    data = json.load(json_file)

pen = render.RenderPen(screen)
tile_map = tiles.TileGrid(data)
a_fake = tiles.FakeGrid()

while True:
    #清空屏幕

    screen.fill("#21263f")

    #逻辑部分

    #帧率改变逻辑
    delta = 60 / (clock.get_fps() + 0.000000000000000000000000000000000000000001)

    #退出游戏
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #移动逻辑
    key = pygame.key.get_pressed()
    pcx = cx
    pcy = cy
    cx += (tcx - cx) * 0.3 * delta
    cy += (tcy - cy) * 0.3 * delta
    if key[pygame.K_a]:
        tcx -= 1
    if key[pygame.K_d]:
        tcx += 1
    if key[pygame.K_s]:
        tcy += 1
    if key[pygame.K_w]:
        tcy -= 1

    #更新角色
    player_idle.update(SCREEN_CENTER[0] - 24, SCREEN_CENTER[1] - 48)

    #格子逻辑
    tile_state = tile_map.get_pos(cx, cy)

    #选择格子
    mouse_pos = pygame.mouse.get_pos()
    a_fake.shift(-cx, -cy)
    mouse_tile_pos = a_fake.in_block(mouse_pos[0], mouse_pos[1])[0]*16 , a_fake.in_block(mouse_pos[0], mouse_pos[1])[1]*16 

    print(a_fake.sx,cx,a_fake.sy,cy)

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
