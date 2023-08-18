from sys import stdin
from tetriscore import Tetris
from blocks import *

block_by_code = {
    'Q': BlockQ(),
    'T': BlockT(),
    'L': BlockL(),
    'J': BlockJ(),
    'Z': BlockZ(),
    'S': BlockS(),
    'I': BlockI()
}

# Main function - reads lines from stdin, decodes blocks and puts it into tetris. Then calculates max height
def process(size: int) -> None:
    for line in stdin:
        codes = line.upper().split(',')
        tetris = Tetris(size)

        for code in codes:
            block = block_by_code.get(code[0])
            if block is None:
                break
            position = int(code[1:])
            tetris.place_block(block, position)

        print(tetris.max_height())

if __name__ == '__main__':
    process(10)
    
