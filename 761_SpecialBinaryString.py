class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str      # Input is a binary string
        :rtype: str       # Output is the largest special binary string
        """
        
        if s == '':
            return ''  
        # If string is empty, return empty string (base case)

        ans = []  
        # List to store special substrings

        cnt = 0  
        # Counter to track balance of '1's and '0's

        i = j = 0  
        # i = current index, j = start index of current special substring

        while i < len(s):  
            # Traverse the string

            cnt += 1 if s[i] == '1' else -1  
            # Increase count for '1', decrease for '0'

            if cnt == 0:  
                # When count becomes 0, we found a valid special substring

                ans.append('1' + self.makeLargestSpecial(s[j + 1:i]) + '0')  
                # Recursively process inner substring and wrap with '1' and '0'

                j = i + 1  
                # Move start index to next position

            i += 1  
            # Move to next character

        ans.sort(reverse=True)  
        # Sort substrings in descending order to make final string largest

        return ''.join(ans)  
        # Join all substrings into one final string