class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        res = []  # List to store all possible results
        for i, c in enumerate(expression):  # Loop through each character with its index
            if c in "+-*":  # If the character is an operator
                left = self.diffWaysToCompute(expression[:i])  # Compute results for left part
                right = self.diffWaysToCompute(expression[i+1:])  # Compute results for right part
                for a in left:  # Loop through all left results
                    for b in right:  # Loop through all right results
                        if c == '+':  # If operator is '+'
                            res.append(a + b)  # Add the sum
                        elif c == '-':  # If operator is '-'
                            res.append(a - b)  # Add the difference
                        else:  # If operator is '*'
                            res.append(a * b)  # Add the product
        if not res:  # If no operator was found (just a number)
            res.append(int(expression))  # Convert string number to int and add it
        return res  # Return all possible results
