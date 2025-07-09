class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        # Find the maximum number of candies any kid currently has
        max_candies = max(candies)
        
        # Create result array by checking if each kid + extraCandies >= max_candies
        # This is more efficient than creating an empty list and appending
        result = [candy + extraCandies >= max_candies for candy in candies]
        
        return result