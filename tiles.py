class TileGrid:
    def __init__(self,start_pos:dict) -> None:
        self.start_pos = start_pos
        self.cx=0
        self.cy=0
    def move(self,x:float,y:float) -> None:
        for tile in self.start_pos:
            tile.x+=x
            tile.y+=y
    def get_pos(self,cx,cy) -> dict:
        self.move(cx-self.x,cy-self.y)
        return self.start_pos
