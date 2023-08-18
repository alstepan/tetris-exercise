
class Block:    
    
    def __init__(self, shape: list[list[int]]):
        self._shape = shape

    # returns the shape of the block
    def shape(self):
        return self._shape
    
    # returns specific cell of the block
    def shape_at(self, y: int, x: int) -> int:
        return self._shape[self.height() - y - 1][x]
    
    def width(self):
        if len(self._shape) > 0:
            return len(self._shape[0])
        else:
            return 0
    
    def height(self):
        return len(self._shape)
    
class Tetris:
    def __init__(self, size: int):
        self._field = []
        self._size = size

    def max_height(self) -> int:
        return len(self._field)
    
    # place block at specific column after determining the most bottom abailable position
    def place_block(self, block: Block, position: int) -> None:
        # find maximum height under the block
        max_height = max([self._max_height_at(position + i) for i in range(block.width())])
        h = max_height + 1
        # moving down the block until it intersects with already placed blocks
        while self._can_place_block_at(block, h, position):
            h -= 1
        #placing block at the position            
        self._place_block_at(block, h + 1, position) 
        #removing completed lines
        self._remove_full_lines()

    # remove all filled lines
    def _remove_full_lines(self) -> None:
        i = 0
        while i < len(self._field):
            blanks = self._field[i].count(0)
            if blanks == 0:
                del self._field[i]
            else:
                i += 1

    # check if block can be placed at specific position
    def _can_place_block_at(self, block: Block, y: int, x: int) -> bool:
        for i in range(block.height()):
            for j in range(block.width()):
                if y + i < 0:
                    return False
                elif len(self._field) <= y + i:
                    continue
                elif self._field[y + i][x + j] != 0 and block.shape_at(i, j) != 0:
                    return False
        return True

    # place block at specific position
    def _place_block_at(self, block: Block, y: int, x: int) -> None:
        if len(self._field) <= y + block.height():
            self._field = self._field + [[0 for x in range(self._size)] for y in range(y + block.height() - len(self._field))]
        for i in range(block.height()):
            for j in range(block.width()):
                if block.shape_at(i, j) != 0:
                    self._field[y + i][x + j] = block.shape_at(i, j)


    # find maximum filled hight at specific column
    def _max_height_at(self, position) -> int:
        height = 0
        i = len(self._field) - 1
        while i > 0:
            if self._field[i][position] != 0:
                height = i
                break
            i -= 1
        return height

