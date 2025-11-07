class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n is 0, only number 0 exists
        if n == 0:
            return 1
        
        # count for n = 1 (0–9 → 10 numbers)
        count = 10
        
        # first digit choices (1–9 → 9 ways)
        unique = 9
        
        # remaining 9 digits (0–9 except first)
        available = 9
        
        # loop while more digits and available digits exist
        while n > 1 and available > 0:
            # multiply by available digits for next place
            unique *= available
            
            # add new unique numbers to total count
            count += unique
            
            # decrease available digits
            available -= 1
            
            # move to next digit length
            n -= 1
        
        # return total count of unique-digit numbers
        return count
