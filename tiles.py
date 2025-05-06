class TileGrid:
    def __init__(self, start_pos: dict) -> None:
        self.start_pos = start_pos
        self.cx = 0
        self.cy = 0
        self.tile_1 = (0, 0)

    def move(self, x: float, y: float) -> None:
        for tile in self.start_pos.items():
            # print(tile)
            tile[1]["x"] += x
            tile[1]["y"] -= y

    def get_pos(self, cx, cy) -> dict:
        self.move(self.cx - cx, cy - self.cy)
        self.cx = cx
        self.cy = cy
        return self.start_pos

    def reload(self, info: dict) -> None:
        self.start_pos = info
        self.get_pos(self.cx, self.cy)


class FakeGrid:
    def __init__(self) -> None:
        self.sx = 0
        self.sy = 0

    def shift(self, x: float, y: float) -> tuple:
        self.sx = x
        self.sy = y

    def in_block(self, x: int, y: int) -> tuple[int, int]:
        return round(x // 16 - self.sx // 16), round(y // 16 - self.sy // 16)
