class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        res = len(nums)  # initialize result with max possible distance
        
        for i, num in enumerate(nums):  # iterate through array with index
            if num == target:  # check if current element matches target
                # update minimum distance from start index
                res = min(res, abs(i - start))
        
        return res  # return the smallest distance found