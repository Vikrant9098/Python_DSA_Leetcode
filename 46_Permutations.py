class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []  # List to store all permutations
        
        # Helper function to perform backtracking
        def backtrack(path, used):
            # If the path length equals nums length, we found a permutation
            if len(path) == len(nums):
                result.append(list(path))  # Add a copy of current path to result
                return
            
            # Try each number in nums
            for i in range(len(nums)):
                if used[i]:  # Skip if number already used
                    continue
                used[i] = True  # Mark as used
                path.append(nums[i])  # Choose the number
                backtrack(path, used)  # Recurse to build further
                path.pop()  # Undo the choice (backtrack)
                used[i] = False  # Mark as unused again
        
        # Start backtracking with empty path and all numbers unused
        backtrack([], [False] * len(nums))
        return result  # Return all generated permutations
