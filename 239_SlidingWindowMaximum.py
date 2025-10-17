class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        dq = deque()  # store indexes of useful elements in decreasing order
        res = []  # result list for max values in each window

        for i in range(len(nums)):
            # remove elements from left if out of current window
            if dq and dq[0] == i - k:
                dq.popleft()

            # remove smaller elements from right (they can’t be max)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)  # add current element’s index

            # once window size is reached, record max (front of deque)
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
