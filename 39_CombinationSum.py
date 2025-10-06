class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []  # List to store all valid combinations
        
        # Helper function for backtracking
        def backtrack(start, path, remain):
            # If remaining target is less than 0, no valid combination
            if remain < 0:
                return
            # If remaining target is 0, we found a valid combination
            if remain == 0:
                result.append(list(path))  # Add a copy of current path
                return
            # Explore all candidates from current index onwards
            for i in range(start, len(candidates)):
                path.append(candidates[i])  # Choose current number
                # Recurse with same index i (since number can be reused)
                backtrack(i, path, remain - candidates[i])
                path.pop()  # Undo the choice (backtrack)
        
        # Start backtracking from index 0 with empty path and full target
        backtrack(0, [], target)
        return result  # Return all valid combinations
