import pygame

class RenderPen:
    def __init__(self,screen:pygame.display.set_mode) -> None:
        self.screen = screen
        self.tiles = []
        for i in range(93):
            self.tiles.append(pygame.transform.scale(pygame.image.load("./assets/tiles/sprite_"+str(i)+".png"),(16,16)))
    def draw(self,type:str,data:dict) -> None:
        if type == "block":
            for block in data.values():
                # print(block)
                if int(block["type"]) > -1:
                    self.screen.blit(self.tiles[int(block["type"])],(block["x"]*16,block["y"]*16))
