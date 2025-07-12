
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Split the string into words, removing extra spaces automatically
        words = s.split()
        
        # Reverse the order of words in the list
        words.reverse()
        
        # Join the reversed words with single spaces
        return ' '.join(words)