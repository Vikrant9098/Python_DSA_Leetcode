class Solution(object):            # Define a class named Solution
    MOD = 10**9 + 7                # Set a constant MOD value for large number modulus

    def countPermutations(self, complexity):   # Function to count valid permutations
        n = len(complexity)        # Get the size of the array
        first = complexity[0]      # Store the first element

        for i in range(1, n):      # Loop through the rest of the array
            if complexity[i] <= first:    # Check if any element is less than or equal to the first
                return 0           # If yes, no valid permutation possible

        fact = 1                   # Start factorial value as 1
        for i in range(2, n):      # Compute factorial from 2 to n-1
            fact = (fact * i) % self.MOD   # Multiply and take modulo

        return fact                # Return the final answer
