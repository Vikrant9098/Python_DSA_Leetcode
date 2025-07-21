class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)                 # Number of cities (size of matrix)
        visited = [False] * n                # Track whether each city is visited
        count = 0                            # Count of provinces

        # Loop through each city
        for i in range(n):
            if not visited[i]:              # If this city hasn't been visited
                self.dfs(isConnected, visited, i)  # Start DFS from this city
                count += 1                  # Increment the province count

        return count                         # Return total number of provinces

    def dfs(self, isConnected, visited, i):
        """
        Perform DFS to visit all cities connected to city i
        """
        visited[i] = True                    # Mark city i as visited

        # Explore all cities connected to i
        for j in range(len(isConnected)):
            # If city i is directly connected to city j and j is unvisited
            if isConnected[i][j] == 1 and not visited[j]:
                self.dfs(isConnected, visited, j)  # Recursively visit city j
