class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = [words[0]]  # Start with the first word in the result list
        
        for i in range(1, len(words)):  # Loop from the second word
            # Sort both current and previous word (from result)
            if sorted(words[i]) != sorted(result[-1]):  # If not anagrams
                result.append(words[i])  # Add current word to result
        
        return result  # Return final list after removing anagrams
