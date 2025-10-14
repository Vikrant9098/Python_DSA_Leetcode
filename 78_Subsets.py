class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []  # list to store all subsets

        # backtracking function
        def backtrack(index, current):
            res.append(list(current))  # add current subset to result

            for i in range(index, len(nums)):
                current.append(nums[i])  # include nums[i] in current subset
                backtrack(i + 1, current)  # move to next element
                current.pop()  # remove last element to backtrack

        backtrack(0, [])  # start from index 0 with empty subset
        return res  # return all subsets
