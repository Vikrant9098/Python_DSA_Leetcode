class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        from collections import deque

        n = len(board)               # size of the board
        target = n * n               # last square

        # BFS queue: stores (current square, moves so far)
        queue = deque([(1, 0)])
        visited = set([1])           # track visited squares

        while queue:
            cell, moves = queue.popleft()  # current square and number of moves

            if cell == target:             # reached last square
                return moves

            # try dice rolls from 1 to 6
            for dice in range(1, 7):
                next_cell = cell + dice
                if next_cell > target:
                    continue

                # get (row, col) for this square
                r, c = self.getCoordinates(next_cell, n)

                # if ladder or snake exists, move to its destination
                if board[r][c] != -1:
                    next_cell = board[r][c]

                # if not visited yet, add to queue
                if next_cell not in visited:
                    visited.add(next_cell)
                    queue.append((next_cell, moves + 1))

        return -1  # cannot reach last square

    # Helper function: convert square number to (row, col)
    def getCoordinates(self, cell, n):
        row = n - 1 - (cell - 1) // n  # row from bottom
        col = (cell - 1) % n            # column from left

        # reverse column for odd rows (zigzag pattern)
        if (n - 1 - row) % 2 == 1:
            col = n - 1 - col

        return row, col
