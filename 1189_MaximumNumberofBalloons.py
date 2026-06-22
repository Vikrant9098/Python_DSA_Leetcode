from collections import Counter

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """

        # Count the frequency of every character present in the string
        f = Counter(text)

        # To form the word "balloon", we need:
        # b -> 1 time
        # a -> 1 time
        # l -> 2 times
        # o -> 2 times
        # n -> 1 time

        # f["l"] >> 1 is equivalent to f["l"] // 2
        # because two 'l' characters are needed for one "balloon"

        # f["o"] >> 1 is equivalent to f["o"] // 2
        # because two 'o' characters are needed for one "balloon"

        # The character with the smallest available count
        # determines how many complete "balloon" words can be formed
        return min(
            f["b"],       # Number of available 'b' characters
            f["a"],       # Number of available 'a' characters
            f["l"] >> 1,  # Number of pairs of 'l' characters
            f["o"] >> 1,  # Number of pairs of 'o' characters
            f["n"]        # Number of available 'n' characters
        )