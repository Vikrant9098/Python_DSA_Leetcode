class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Edge case: if lengths differ → can't be isomorphic
        if len(s) != len(t):
            return False

        # Dictionaries to track character mappings
        mapS = {}  # s -> t mapping
        mapT = {}  # t -> s mapping

        for i in range(len(s)):
            chS = s[i]  # Current character in s
            chT = t[i]  # Current character in t

            # If mappings exist and don't match → not isomorphic
            if (chS in mapS and mapS[chS] != chT) or (chT in mapT and mapT[chT] != chS):
                return False

            # Store mapping
            mapS[chS] = chT
            mapT[chT] = chS

        return True  # All characters match mapping → isomorphic
