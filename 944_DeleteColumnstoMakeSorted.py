class Solution(object):                 # Define a class named Solution
    def minDeletionSize(self, A):        # Function to count columns to delete

        ret = 0                          # Variable to store number of bad columns
        
        for c in zip(*A):                # Loop through each column using zip
            if list(c) != sorted(c):     # Check if column is not sorted
                ret += 1                 # Increase count if column is unsorted
                
        return ret                       # Return total columns to delete
