class Solution:
  def minimumSum(self, grid):
    m = len(grid)                     # number of rows
    n = len(grid[0])                  # number of columns
    ans = m * n                       # initialize answer with max possible area

    # Case 1: Split horizontally (top + bottom parts, then split bottom into two)
    for i in range(m):
      top = self._minimumArea(grid, 0, i, 0, n - 1)   # area of rectangle in top part
      for j in range(n):
        ans = min(ans, top +                        # top part
                  self._minimumArea(grid, i + 1, m - 1, 0, j) +       # bottom-left
                  self._minimumArea(grid, i + 1, m - 1, j + 1, n - 1)) # bottom-right

    # Case 2: Split horizontally (bottom + top parts, then split top into two)
    for i in range(m):
      bottom = self._minimumArea(grid, i, m - 1, 0, n - 1)   # area of rectangle in bottom part
      for j in range(n):
        ans = min(ans, bottom +                     # bottom part
                  self._minimumArea(grid, 0, i - 1, 0, j) +       # top-left
                  self._minimumArea(grid, 0, i - 1, j + 1, n - 1)) # top-right

    # Case 3: Split vertically (left + right parts, then split right into two)
    for j in range(n):
      left = self._minimumArea(grid, 0, m - 1, 0, j)    # area of rectangle in left part
      for i in range(m):
        ans = min(ans, left +                       # left part
                  self._minimumArea(grid, 0, i, j + 1, n - 1) +     # right-top
                  self._minimumArea(grid, i + 1, m - 1, j + 1, n - 1)) # right-bottom

    # Case 4: Split vertically (right + left parts, then split left into two)
    for j in range(n):
      right = self._minimumArea(grid, 0, m - 1, j, n - 1)  # area of rectangle in right part
      for i in range(m):
        ans = min(ans, right +                      # right part
                  self._minimumArea(grid, 0, i, 0, j - 1) +        # left-top
                  self._minimumArea(grid, i + 1, m - 1, 0, j - 1)) # left-bottom

    # Case 5: Split into 3 horizontal bands
    for i1 in range(m):
      for i2 in range(i1 + 1, m):
        ans = min(ans,
                  self._minimumArea(grid, 0, i1, 0, n - 1) +       # top band
                  self._minimumArea(grid, i1 + 1, i2, 0, n - 1) +  # middle band
                  self._minimumArea(grid, i2 + 1, m - 1, 0, n - 1))# bottom band

    # Case 6: Split into 3 vertical bands
    for j1 in range(n):
      for j2 in range(j1 + 1, n):
        ans = min(ans,
                  self._minimumArea(grid, 0, m - 1, 0, j1) +       # left band
                  self._minimumArea(grid, 0, m - 1, j1 + 1, j2) +  # middle band
                  self._minimumArea(grid, 0, m - 1, j2 + 1, n - 1))# right band

    return ans   # return smallest total area

  # Helper function to find min rectangle covering all 1s in given subgrid
  def _minimumArea(self, grid, si, ei, sj, ej):
    x1 = float('inf')  # smallest row index of 1
    y1 = float('inf')  # smallest col index of 1
    x2 = -1            # largest row index of 1
    y2 = -1            # largest col index of 1
    for i in range(si, ei + 1):      # loop over rows in subgrid
      for j in range(sj, ej + 1):    # loop over cols in subgrid
        if grid[i][j] == 1:          # if we find a 1
          x1 = min(x1, i)            # update min row
          y1 = min(y1, j)            # update min col
          x2 = max(x2, i)            # update max row
          y2 = max(y2, j)            # update max col
    return 0 if x1 == float('inf') else (x2 - x1 + 1) * (y2 - y1 + 1)  
    # if no 1s found → return 0, else return area of bounding box
