class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Helper to get the sorted digits as a string
        def sort_digits(x):
            return ''.join(sorted(str(x)))
        
        # Precompute sorted strings for all powers of two up to 10^9
        power_of_two_patterns = {sort_digits(1 << i) for i in range(31)}
        
        # Check if sorted digits of n match any power of two's digits
        return sort_digits(n) in power_of_two_patterns
