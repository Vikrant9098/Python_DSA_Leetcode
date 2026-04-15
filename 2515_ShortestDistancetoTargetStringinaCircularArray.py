class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        ans = n = len(words)  # Initialize answer with max possible distance (n)

        # Traverse all words with index
        for i, word in enumerate(words):
            if word == target:  # Check if current word matches target
                # Calculate minimum circular distance:
                # direct distance = abs(i - startIndex)
                # circular distance = n - abs(i - startIndex)
                ans = min(ans, abs(i - startIndex), n - abs(i - startIndex))

        # If ans is updated, return it; otherwise return -1 (target not found)
        return ans if ans < n else -1