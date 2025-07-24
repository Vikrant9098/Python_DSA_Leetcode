class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Base case: T0 = 0
        if n == 0:
            return 0
        
        # Base case: T1 = 1
        if n == 1:
            return 1

        # Base case: T2 = 1
        if n == 2:
            return 1

        # Initialize first three values of the Tribonacci sequence
        t0 = 0  # Represents T0
        t1 = 1  # Represents T1
        t2 = 1  # Represents T2

        # Loop from 3 to n to calculate the nth tribonacci number
        for i in range(3, n + 1):
            # Current Tn is sum of previous three
            t3 = t0 + t1 + t2

            # Shift the values for next iteration
            t0 = t1      # Tn-3 becomes Tn-2
            t1 = t2      # Tn-2 becomes Tn-1
            t2 = t3      # Tn-1 becomes current Tn

        # After the loop, t2 will have the value of Tn
        return t2
