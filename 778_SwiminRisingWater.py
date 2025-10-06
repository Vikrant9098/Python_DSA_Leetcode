import heapq

class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)  # Get grid size (n x n)
        visited = [[False] * n for _ in range(n)]  # Track visited cells
        
        # Min-heap (priority queue): stores (elevation, row, col)
        heap = [(grid[0][0], 0, 0)]
        visited[0][0] = True  # Mark starting cell as visited
        
        # 4 possible directions (down, up, right, left)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        time = 0  # Tracks the maximum elevation on our path so far
        
        while heap:
            height, r, c = heapq.heappop(heap)  # Get cell with smallest elevation
            time = max(time, height)  # Update time with max elevation seen so far
            
            # If we reached the bottom-right cell, return the time
            if r == n - 1 and c == n - 1:
                return time
            
            # Explore all 4 adjacent cells
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check boundaries and if cell not visited
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True  # Mark cell as visited
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))  # Add to heap
        
        return -1  # Should never reach here
