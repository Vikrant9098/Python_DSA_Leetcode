class Solution(object):
    def maximumEnergy(self, energy, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        n = len(energy)              # Get the number of magicians
        dp = [0] * n                 # Create a list to store max energy from each magician
        max_energy = float('-inf')   # Start with the smallest possible number
        
        # Loop from last magician to the first
        for i in range(n - 1, -1, -1):
            if i + k >= n:           # If next jump goes out of range
                dp[i] = energy[i]    # Only take current magician's energy
            else:                    # If jump is within range
                dp[i] = energy[i] + dp[i + k]  # Add current energy and next jump's total energy
            max_energy = max(max_energy, dp[i])  # Keep track of the maximum energy
        
        return max_energy            # Return the highest energy possible
