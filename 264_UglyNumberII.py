class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [0] * n           # Array to store ugly numbers
        ugly[0] = 1              # First ugly number is always 1

        i2 = i3 = i5 = 0         # Pointers for multiples of 2, 3, and 5
        next2, next3, next5 = 2, 3, 5  # Next possible ugly numbers

        for i in range(1, n):    # Generate ugly numbers from 2nd to nth
            next_ugly = min(next2, next3, next5)  # Pick the smallest among 2, 3, 5
            ugly[i] = next_ugly  # Store it in the list

            if next_ugly == next2:   # If chosen number came from 2’s list
                i2 += 1              # Move 2’s pointer ahead
                next2 = ugly[i2] * 2 # Update next multiple of 2

            if next_ugly == next3:   # If chosen number came from 3’s list
                i3 += 1              # Move 3’s pointer ahead
                next3 = ugly[i3] * 3 # Update next multiple of 3

            if next_ugly == next5:   # If chosen number came from 5’s list
                i5 += 1              # Move 5’s pointer ahead
                next5 = ugly[i5] * 5 # Update next multiple of 5

        return ugly[-1]          # Return the nth ugly number
