class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int      # starting number of range
        :type right: int     # ending number of range
        :rtype: int          # returns count of numbers with prime set bits
        """
        
        count = 0  # This will store how many numbers have prime number of set bits
        
        # Loop through every number from left to right (inclusive)
        for i in range(left, right + 1):
            
            # Convert number to binary and count how many '1's are present
            # '1's in binary representation are called set bits
            setBits = bin(i).count('1')
            
            # Check if number of set bits is prime
            if self.isPrime(setBits):
                count += 1  # If prime, increase count
        
        return count  # Return final count
    
    
    def isPrime(self, n):
        """
        :type n: int     # number to check
        :rtype: bool     # returns True if prime, else False
        """
        
        # Numbers less than or equal to 1 are not prime
        if n <= 1:
            return False
        
        # Check divisibility from 2 up to square root of n
        # If divisible by any number, it is not prime
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False  # Not prime
        
        return True  # If no divisors found, it is prime