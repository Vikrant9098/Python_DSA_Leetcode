class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)  # get the length of the list
        sorted_nums = sorted(nums)  # make a sorted copy of the list
        
        mid = (n + 1) // 2  # find the middle index
        j = mid - 1  # pointer for the smaller half
        k = n - 1    # pointer for the larger half
        
        # fill the list in wiggle pattern
        for i in range(n):
            if i % 2 == 0:  # even index takes from smaller half
                nums[i] = sorted_nums[j]
                j -= 1
            else:           # odd index takes from larger half
                nums[i] = sorted_nums[k]
                k -= 1
