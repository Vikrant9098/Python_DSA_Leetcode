class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        # Dictionary to store frequency of each remainder
        remainder_count = {}
        
        # Count remainders (handle negative numbers properly)
        for num in nums:
            remainder = ((num % value) + value) % value  # normalize remainder
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1
        
        mex = 0  # start checking from 0
        
        # Keep increasing mex until we can't form it
        while True:
            remainder = mex % value  # find remainder for current number
            if remainder_count.get(remainder, 0) > 0:  # if remainder exists
                remainder_count[remainder] -= 1  # use one occurrence
                mex += 1  # check next number
            else:
                return mex  # can't form this number, so return it
