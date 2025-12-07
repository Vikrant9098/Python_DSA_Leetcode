class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        
        nums = high - low + 1      # total numbers in the range
        
        if low % 2 != 0 and high % 2 != 0:  # if both low and high are odd
            return nums // 2 + 1            # odds = half + 1
        else:
            return nums // 2                # otherwise odds = half
