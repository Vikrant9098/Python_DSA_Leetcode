class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # Base case: first term is always "1"
        if n == 1:
            return "1"

        # Start with "1"
        result = "1"

        # Loop from 2 to n
        for i in range(2, n + 1):
            temp = ""              # to store next sequence
            count = 1              # count same digits
            prev = result[0]       # first character

            # Loop through the string from second char
            for j in range(1, len(result)):
                curr = result[j]   # current character
                if curr == prev:   # if same as previous
                    count += 1     # increase count
                else:
                    temp += str(count) + prev  # add count and digit
                    prev = curr                # move to new digit
                    count = 1                  # reset count

            # Add the last group (count and digit)
            temp += str(count) + prev

            # Update result for next round
            result = temp

        # Return the final result
        return result
