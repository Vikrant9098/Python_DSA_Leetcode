class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)  # get total number of words
        masks = [0] * n  # create list to store bitmask of each word
        lens = [0] * n   # create list to store length of each word

        # loop through each word
        for i in range(n):
            mask = 0  # start with 0 bitmask
            for c in words[i]:  # loop through each character
                mask |= 1 << (ord(c) - ord('a'))  # set bit for the character
            masks[i] = mask  # save bitmask for this word
            lens[i] = len(words[i])  # save length of this word

        max_product = 0  # store the maximum product found

        # check all pairs of words
        for i in range(n):
            for j in range(i + 1, n):  # compare word i with word j
                if (masks[i] & masks[j]) == 0:  # if no common letters
                    product = lens[i] * lens[j]  # multiply their lengths
                    max_product = max(max_product, product)  # update max if larger

        return max_product  # return the final maximum product
