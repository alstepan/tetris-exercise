from tetriscore import Block

class BlockQ(Block):
    def __init__(self):
        Block.__init__(self, 
            [
            [1, 1], 
            [1, 1]
            ]
        )

class BlockZ(Block):
    def __init__(self):
        Block.__init__(self, 
            [
                [1, 1, 0], 
                [0, 1, 1]
            ]
        )

class BlockS(Block):
    def __init__(self):
        Block.__init__(self, 
            [
                [0, 1, 1], 
                [1, 1, 0]
            ]
        )

class BlockT(Block):
    def __init__(self):
        Block.__init__(self, 
            [
                [1, 1, 1],
                [0, 1, 0]
            ]
        )

class BlockI(Block):
    def __init__(self):
        Block.__init__(self, [[1, 1, 1, 1]])

class BlockL(Block):
    def __init__(self):
        Block.__init__(self, 
            [
                [1, 0], 
                [1, 0],
                [1, 1,]
            ]
        )

class BlockJ(Block):
    def __init__(self):
        Block.__init__(self, 
            [
                [0, 1], 
                [0, 1],
                [1, 1]
            ]
        )