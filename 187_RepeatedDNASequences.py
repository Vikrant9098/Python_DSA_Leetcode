class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()           # stores all unique 10-letter sequences
        repeated = set()       # stores sequences that appear more than once
        n = len(s)

        for i in range(n - 9):             # loop till last possible 10-letter substring
            sub = s[i:i + 10]              # get 10-letter substring
            if sub in seen:                # if already seen before
                repeated.add(sub)          # add to repeated set
            else:
                seen.add(sub)              # otherwise mark as seen

        return list(repeated)              # return all repeated substrings as list
