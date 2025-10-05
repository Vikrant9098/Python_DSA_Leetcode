class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []  # List to store all combinations

        # Helper function for backtracking
        def backtrack(start, path):
            if len(path) == k:  # If combination size equals k
                result.append(list(path))  # Add a copy of current combination
                return
            for i in range(start, n + 1):  # Loop through numbers from start to n
                path.append(i)  # Add current number to combination
                backtrack(i + 1, path)  # Recurse with next number
                path.pop()  # Backtrack, remove last number

        backtrack(1, [])  # Start backtracking from 1 with empty path
        return result
