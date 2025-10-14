class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []  # store all palindrome partitions

        # backtracking function to generate partitions
        def backtrack(start, current):
            if start == len(s):  # reached end of string
                res.append(list(current))  # add current partition to result
                return

            for end in range(start, len(s)):  # try every possible end index
                if isPalindrome(start, end):  # check if substring is palindrome
                    current.append(s[start:end+1])  # add substring to current partition
                    backtrack(end + 1, current)  # move to next start index
                    current.pop()  # backtrack: remove last substring

        # helper function to check if substring s[left..right] is palindrome
        def isPalindrome(left, right):
            while left < right:  # compare characters from both ends
                if s[left] != s[right]:
                    return False  # not palindrome
                left += 1  # move left pointer right
                right -= 1  # move right pointer left
            return True  # substring is palindrome

        backtrack(0, [])  # start backtracking from index 0 with empty list
        return res  # return all valid palindrome partitions
