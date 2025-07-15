class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # If lengths are different, strings cannot be close
        if len(word1) != len(word2):
            return False
        
        # Count frequency of each character in both strings
        count1 = {}
        count2 = {}
        
        for char in word1:
            count1[char] = count1.get(char, 0) + 1
        
        for char in word2:
            count2[char] = count2.get(char, 0) + 1
        
        # Check if both strings have the same set of characters
        # Operation 2 requires that characters exist in both strings
        if set(count1.keys()) != set(count2.keys()):
            return False
        
        # Check if the frequency distributions are the same
        # Operation 2 allows us to swap frequency counts between characters
        return sorted(count1.values()) == sorted(count2.values())