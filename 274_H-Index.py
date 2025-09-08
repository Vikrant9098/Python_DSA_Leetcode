class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # Sort citations in descending order
        citations.sort(reverse=True)
        
        h = 0  # Start with h = 0
        # Loop through each paper
        for i, c in enumerate(citations):
            # If current paper has at least i+1 citations
            if c >= i + 1:
                h = i + 1  # update h
            else:
                break  # stop, since further citations will be smaller
        return h
