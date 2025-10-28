class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordSet = set(wordDict)          # convert list to set for faster lookup
        memo = {}                        # memoization dictionary

        def backtrack(subs):
            if subs in memo:             # if already solved, return stored result
                return memo[subs]
            if not subs:                 # if string is empty
                return [""]              # return list with empty string

            res = []                     # list to store valid sentences
            for word in wordSet:         # check every word in dictionary
                if subs.startswith(word):    # if prefix matches
                    rest = subs[len(word):]  # remaining string
                    subSentences = backtrack(rest)  # recursive call for rest
                    for sub in subSentences:        # combine results
                        space = "" if sub == "" else " "
                        res.append(word + space + sub)

            memo[subs] = res              # store result in memo
            return res                    # return all sentences for this substring

        return backtrack(s)               # start recursion with full string
