import bisect

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # List to store the smallest tail of all increasing subsequences
        sub = []

        for num in nums:
            # Find the index where num can be inserted to maintain increasing order
            i = bisect.bisect_left(sub, num)

            # If num is larger than all elements, append it
            if i == len(sub):
                sub.append(num)
            # Otherwise, replace the first element >= num
            else:
                sub[i] = num

        # Length of sub is the length of the longest increasing subsequence
        return len(sub)
