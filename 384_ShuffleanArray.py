import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = list(nums)   # store original array
        self.array = list(nums)      # store current (shuffled) array

    def reset(self):
        """
        :rtype: List[int]
        """
        self.array = list(self.original)  # reset array to original
        return self.array                 # return original array

    def shuffle(self):
        """
        :rtype: List[int]
        """
        arr = list(self.array)            # make a copy to shuffle
        n = len(arr)                      # get array length
        for i in range(n - 1, 0, -1):     # loop from end to start
            j = random.randint(0, i)      # pick random index 0 to i
            arr[i], arr[j] = arr[j], arr[i]  # swap elements
        return arr                        # return shuffled array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
