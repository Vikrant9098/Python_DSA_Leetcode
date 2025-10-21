class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()             # Sort array to handle duplicates easily
        result = []             # List to store all subsets

        def backtrack(start, tempList):
            result.append(list(tempList))  # Add current subset to result
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:  # Skip duplicates
                    continue
                tempList.append(nums[i])        # Include current number
                backtrack(i + 1, tempList)      # Recurse for next elements
                tempList.pop()                  # Backtrack, remove last number

        backtrack(0, [])        # Start backtracking from index 0
        return result           # Return final list of subsets
