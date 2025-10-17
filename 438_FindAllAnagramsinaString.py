class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []  # list to store starting indices of anagrams
        if len(s) < len(p):
            return res  # if s is smaller than p, no anagram possible

        p_count = [0] * 26  # frequency of letters in p
        s_count = [0] * 26  # frequency of letters in current window of s

        for c in p:
            p_count[ord(c) - ord('a')] += 1  # count each character in p

        window = len(p)  # size of the sliding window

        for i in range(len(s)):
            s_count[ord(s[i]) - ord('a')] += 1  # add current character to window count

            if i >= window:
                # remove character left out of window
                s_count[ord(s[i - window]) - ord('a')] -= 1

            if s_count == p_count:  # if counts match, we found an anagram
                res.append(i - window + 1)  # add starting index

        return res
