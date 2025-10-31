class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)           # total number of papers
        left, right = 0, n - 1       # binary search boundaries
        
        # Perform binary search
        while left <= right:
            mid = (left + right) // 2    # find middle index
            h = n - mid                  # number of papers with at least citations[mid] citations
            
            if citations[mid] == h:      # exact match found
                return h
            elif citations[mid] < h:     # need more citations, move right
                left = mid + 1
            else:                        # too many citations, move left
                right = mid - 1
        
        return n - left                  # final h-index after search
