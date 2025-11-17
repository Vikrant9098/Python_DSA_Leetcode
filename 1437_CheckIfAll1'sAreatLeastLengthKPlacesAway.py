class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        last = -1  # index of previous 1 (start as -1 meaning no 1 seen yet)

        for i in range(len(nums)):   # loop through array
            if nums[i] == 1:         # found a 1
                if last != -1 and (i - last - 1) < k:  # check distance from previous 1
                    return False     # distance smaller than k → not valid
                last = i             # update previous 1 index
        
        return True  # all 1s are k places apart
