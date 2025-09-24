class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Stack to store previous results and signs when encountering '('
        stack = []   
        # Current calculated result
        result = 0   
        # Current sign (+1 for '+', -1 for '-')
        sign = 1     
        # Number currently being read (could have multiple digits)
        number = 0   
        
        # Index to traverse the string
        i = 0
        while i < len(s):
            c = s[i]  # current character
            
            if c.isdigit():
                # Build the current number (handle multiple digits)
                number = number * 10 + int(c)
            elif c == '+':
                # Add the previous number with its sign
                result += sign * number
                number = 0          # reset number
                sign = 1            # set sign to positive
            elif c == '-':
                # Add the previous number with its sign
                result += sign * number
                number = 0          # reset number
                sign = -1           # set sign to negative
            elif c == '(':
                # Push the current result and sign onto the stack
                stack.append(result)
                stack.append(sign)
                # Reset for evaluating inside parentheses
                result = 0
                sign = 1
            elif c == ')':
                # Add the last number before closing parenthesis
                result += sign * number
                number = 0
                # Pop the sign before '('
                result *= stack.pop()  
                # Pop the result calculated before '('
                result += stack.pop()  
            # Ignore spaces and move to the next character
            i += 1
        
        # Add the last number (if any) after finishing traversal
        result += sign * number
        # Return final calculated result
        return result
