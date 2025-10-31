class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set()              # To keep track of numbers already seen
        duplicates = []           # To store duplicate numbers
        
        for num in nums:          # Loop through each number
            if num in seen:       # If number is already seen, it's a duplicate
                duplicates.append(num)  # Add duplicate to the list
            else:
                seen.add(num)     # Otherwise, mark it as seen
        
        return duplicates         # Return the two sneaky numbers
