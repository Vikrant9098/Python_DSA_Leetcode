class Robot(object):

    def __init__(self, width, height):
        """
        Initialize robot with grid dimensions
        """
        self.w = width      # width of grid
        self.h = height     # height of grid
        
        # total steps to complete one full boundary cycle (perimeter)
        self.p = 2 * (width - 1) + 2 * (height - 1)
        
        self.curr = 0       # current position index on boundary
        self.moved = False  # track if robot has moved at least once

    def step(self, num):
        """
        Move robot num steps along the boundary
        """
        self.moved = True   # mark that robot has moved
        
        # move forward and wrap using modulo (circular path)
        self.curr = (self.curr + num) % self.p

    def getPos(self):
        """
        Return current (x, y) position
        """
        idx = self.curr
        w = self.w
        h = self.h

        # CASE 1: bottom row (moving right)
        if idx < w:
            return [idx, 0]

        # CASE 2: right column (moving up)
        if idx < w + h - 1:
            return [w - 1, idx - (w - 1)]

        # CASE 3: top row (moving left)
        if idx < 2 * w + h - 2:
            return [w - 1 - (idx - (w + h - 2)), h - 1]

        # CASE 4: left column (moving down)
        return [0, h - 1 - (idx - (2 * w + h - 3))]

    def getDir(self):
        """
        Return current direction of robot
        """
        idx = self.curr
        w = self.w
        h = self.h

        # before any move : default direction is East
        if not self.moved:
            return "East"

        # special case: back to start after moving -> facing South
        if idx == 0:
            return "South"

        # bottom row -> moving right
        if 1 <= idx <= w - 1:
            return "East"

        # right column -> moving up
        if w <= idx <= w + h - 2:
            return "North"

        # top row -> moving left
        if w + h - 1 <= idx <= 2 * w + h - 3:
            return "West"

        # left column -> moving down
        return "South"