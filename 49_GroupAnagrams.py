class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        
        # Dictionary where key = sorted word, value = list of anagrams
        anagrams = defaultdict(list)
        
        for word in strs:
            # Sort the word (all anagrams will have same sorted string)
            key = ''.join(sorted(word))
            
            # Add the word into the correct group
            anagrams[key].append(word)
        
        # Return all groups as a list of lists
        return list(anagrams.values())
