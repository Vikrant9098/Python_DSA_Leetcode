class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Count occurrences of each element
        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1
        
        # Get all occurrence counts
        occurrences = list(count.values())
        
        # Check if all occurrence counts are unique
        # If length of set equals length of list, all elements are unique
        return len(set(occurrences)) == len(occurrences)