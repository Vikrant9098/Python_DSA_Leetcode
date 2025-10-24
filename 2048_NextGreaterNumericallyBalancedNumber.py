class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Loop through numbers greater than n up to 1224444
        # (1224444 is the largest possible numerically balanced number)
        for i in range(n + 1, 1224445):
            
            # Check if the current number is numerically balanced
            if self.isBalanced(i):
                # If yes, return it as the answer
                return i

        # Return -1 if no such number found (this normally won't happen)
        return -1

    # Helper function to check if a number is numerically balanced
    def isBalanced(self, num):
        # Convert the number to string for easy digit processing
        s = str(num)
        
        # Dictionary to store count of each digit
        count = {}
        
        # Count the occurrences of each digit
        for c in s:
            # Convert character to integer digit
            d = int(c)
            # Increase count of this digit in the dictionary
            count[d] = count.get(d, 0) + 1
        
        # Check if each digit appears exactly 'd' times
        for d in count:
            # If a digit appears but not exactly 'd' times, return False
            if count[d] != d:
                return False
        
        # If all digits satisfy the balanced condition, return True
        return True
