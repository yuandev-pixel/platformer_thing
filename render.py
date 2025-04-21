import pygame

class RenderPen:
    def __init__(self,screen:pygame.display.set_mode) -> None:
        self.screen = screen
    def draw(self,type:str,data:dict) -> None:
        if type == "block":
            for block in data.values():
                # print(block)
                self.screen.blit(pygame.transform.scale(pygame.image.load("./assets/tiles/sprite_"+block["type"]+".png"),(16,16)),(block["x"]*16,block["y"]*16))
