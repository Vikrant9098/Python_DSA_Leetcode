    class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums[:]                # store original array
        self.n = len(nums)                 # length of array
        self.bit = [0] * (self.n + 1)      # Binary Indexed Tree (1-indexed)

        # build the BIT
        for i in range(self.n):
            self._init(i, nums[i])         # initialize BIT with nums values

    def _init(self, i, val):
        """helper to update BIT during initialization"""
        i += 1                             # convert to 1-indexed
        while i <= self.n:
            self.bit[i] += val             # add value to current BIT node
            i += (i & -i)                  # move to next responsible node

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        diff = val - self.nums[index]      # find difference from old value
        self.nums[index] = val             # update actual array
        self._init(index, diff)            # update BIT with difference

    def _getSum(self, i):
        """helper to get prefix sum up to index i"""
        s = 0
        i += 1                             # convert to 1-indexed
        while i > 0:
            s += self.bit[i]               # add current BIT value
            i -= (i & -i)                  # move to parent node
        return s

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # range sum = prefix(right) - prefix(left - 1)
        return self._getSum(right) - self._getSum(left - 1)
