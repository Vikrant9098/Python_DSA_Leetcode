class Solution(object):                      # Define the Solution class
    def maximumHappinessSum(self, happiness, k):  # Function to calculate maximum happiness
        """
        :type happiness: List[int]           # List of happiness values
        :type k: int                         # Number of children to choose
        :rtype: int                          # Return type is integer
        """
        h = sorted(happiness, reverse=True)  # Sort happiness in descending order
        res = 0                              # Store total happiness

        for i in range(k):                   # Loop for k children
            if h[i] <= i:                    # If happiness becomes zero or negative
                return res                   # Stop and return result
            res += h[i] - i                  # Add reduced happiness to result

        return res                           # Return final happiness sum
