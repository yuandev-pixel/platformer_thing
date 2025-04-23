class TileGrid:
    def __init__(self,start_pos:dict) -> None:
        self.start_pos = start_pos
        self.cx=0
        self.cy=0
    def move(self,x:float,y:float) -> None:
        for tile in self.start_pos.items():
            # print(tile)
            tile[1]["x"]+=x
            tile[1]["y"]+=y
    def get_pos(self,cx,cy) -> dict:
        self.move(self.cx-cx,cy-self.cy)
        self.cx = cx
        self.cy = cy
        return self.start_pos
