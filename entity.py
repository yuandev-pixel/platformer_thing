import pygame

class Entity:
    def __init__(self, x:int, y:int,image:pygame.Surface,hitbox:pygame.Rect) -> None:
        self.x = x
        self.y = y
        self.image = image
        self.hitbox = hitbox

    def draw(self, screen:pygame.Surface) -> None:
        screen.blit(self.image, (self.x, self.y))
