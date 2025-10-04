import heapq  # Import heapq for using a priority queue (min-heap)

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        # If the map is empty or too small, no water can be trapped
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])  # Dimensions of the matrix
        visited = [[False] * n for _ in range(m)]  # Keep track of visited cells
        heap = []  # Min-heap to store boundary cells

        # Step 1: Push all the boundary cells into the heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))  # (height, row, col)
                    visited[i][j] = True  # Mark boundary as visited

        total_water = 0  # To store total trapped water
        directions = [(1,0), (-1,0), (0,1), (0,-1)]  # Four directions (up, down, left, right)

        # Step 2: Process cells from the heap (starting from lowest boundary)
        while heap:
            height, x, y = heapq.heappop(heap)  # Get the lowest boundary cell

            # Check all 4 directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # Skip if out of bounds or already visited
                if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny]:
                    continue

                visited[nx][ny] = True  # Mark as visited

                # If the neighbor is lower, water can be trapped
                total_water += max(0, height - heightMap[nx][ny])

                # Push the neighbor into the heap with max(height, neighbor height)
                # Because this determines the new boundary level
                heapq.heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))

        return total_water  # Return the total trapped water
