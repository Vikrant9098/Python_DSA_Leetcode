class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math  # To use factorial function
        numbers = [str(i) for i in range(1, n + 1)]  # List of numbers as strings
        k -= 1  # Convert k to 0-based index
        result = []  # To store the permutation result

        # Build the kth permutation
        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)  # Compute (i-1)!
            index = k // fact  # Find which number to choose
            result.append(numbers[index])  # Add that number to result
            numbers.pop(index)  # Remove used number
            k %= fact  # Update k for next position

        return ''.join(result)  # Join list into string and return
