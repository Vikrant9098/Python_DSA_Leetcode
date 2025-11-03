class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_index = {c: i for i, c in enumerate(s)}  # store last index of each char
        stack = []  # used to build the result string
        seen = set()  # track if a character is already in the stack

        # iterate through each character
        for i, c in enumerate(s):
            if c in seen:  # skip if already in stack
                continue

            # remove characters that are greater than current and appear later
            while stack and c < stack[-1] and last_index[stack[-1]] > i:
                seen.remove(stack.pop())  # remove from stack and mark unseen

            stack.append(c)  # add current character
            seen.add(c)  # mark as seen

        return "".join(stack)  # combine stack into result string
