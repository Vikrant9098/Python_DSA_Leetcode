class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int      # Length of happy string
        :type k: int      # We need the k-th happy string
        :rtype: str       # Return type is string
        """
        
        # DFS function to build happy strings
        def dfs(path=''):
            
            # If we already found k strings, stop recursion (optimization)
            if len(res) == k:
                return
            
            # If current string length becomes n,
            # it means we formed a valid happy string
            if len(path) == n:
                return res.append(path)   # Store it in result list
            
            # Try all possible characters
            for x in 'abc':
                
                # Add character only if:
                # 1) path is empty OR
                # 2) current character is not same as previous character
                # (because happy string cannot have consecutive same letters)
                if not path or x != path[-1]:
                    dfs(path + x)   # Recursively build next character
        
        res = []   # List to store valid happy strings
        
        dfs()      # Start DFS with empty string
        
        # If we found at least k happy strings,
        # return the k-th one (last added)
        # Otherwise return empty string
        return res[-1] if len(res) == k else ''