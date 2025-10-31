class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0                      # Step 1: XOR all numbers to get xor = a ^ b
        for num in nums:
            xor ^= num               # Cancels out pairs, leaving a ^ b

        diff = xor & -xor            # Step 2: Find rightmost set bit (difference between a and b)

        a = 0
        b = 0
        for num in nums:             # Step 3: Divide into two groups based on the set bit
            if num & diff:
                a ^= num             # XOR numbers with the bit set
            else:
                b ^= num             # XOR numbers without the bit set

        return [a, b]                # Step 4: Return the two unique numbers
