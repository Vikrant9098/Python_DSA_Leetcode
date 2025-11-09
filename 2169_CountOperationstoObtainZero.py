class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        count = 0  # to store number of operations
        
        # continue until either number becomes 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 -= num2  # subtract smaller number from larger
            else:
                num2 -= num1  # subtract smaller number from larger
            count += 1  # increment operation count
        
        return count  # return total number of operations
