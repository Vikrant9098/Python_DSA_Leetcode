class Solution:

    def dfs(self, arr, idx, vis):

        if idx < 0 or idx >= len(arr) or vis[idx]:
            return False

        if arr[idx] == 0:
            return True

        vis[idx] = True

        return (self.dfs(arr, idx + arr[idx], vis) or
                self.dfs(arr, idx - arr[idx], vis))

    def canReach(self, arr, start):

        vis = [False] * len(arr)

        return self.dfs(arr, start, vis)class Solution:

    def dfs(self, arr, idx, vis):

        if idx < 0 or idx >= len(arr) or vis[idx]:
            return False

        if arr[idx] == 0:
            return True

        vis[idx] = True

        return (self.dfs(arr, idx + arr[idx], vis) or
                self.dfs(arr, idx - arr[idx], vis))

    def canReach(self, arr, start):

        vis = [False] * len(arr)

        return self.dfs(arr, start, vis)