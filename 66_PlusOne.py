class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)  # get the length of the list
        
        # Traverse digits from the end (least significant digit)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1  # increment digit if less than 9
                return digits   # no carry, return result
            digits[i] = 0       # if digit is 9, set to 0 and carry over
        
        # If all digits were 9, need a new list with extra digit
        result = [0] * (n + 1)
        result[0] = 1         # first digit is 1, rest are 0
        return result
