class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []  # To store all unique permutations
        nums.sort()  # Sort to easily skip duplicates
        used = [False] * len(nums)  # Track which elements are already used

        def backtrack(path):
            # Base case: when current path has all numbers
            if len(path) == len(nums):
                res.append(list(path))  # Add a copy of the current permutation
                return

            for i in range(len(nums)):
                # Skip used elements
                if used[i]:
                    continue

                # Skip duplicates: if current number same as previous and previous was not used
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                # Choose the current number
                used[i] = True
                path.append(nums[i])

                # Explore further
                backtrack(path)

                # Undo the choice (backtrack)
                path.pop()
                used[i] = False

        backtrack([])  # Start backtracking with an empty path
        return res
