class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # Initialize an empty stack to store numbers
        stack = []  
        
        # Loop through each token in the input list
        for token in tokens:
            # Check if the token is an operator
            if token in {"+", "-", "*", "/"}:
                # Pop the second operand (top of stack)
                b = stack.pop()
                # Pop the first operand (next top)
                a = stack.pop()
                
                # Perform the operation based on the operator
                if token == "+":
                    stack.append(a + b)  # addition
                elif token == "-":
                    stack.append(a - b)  # subtraction
                elif token == "*":
                    stack.append(a * b)  # multiplication
                elif token == "/":
                    # Division truncates toward zero; convert to float first
                    stack.append(int(a / float(b)))
            else:
                # If token is a number, convert it to int and push onto stack
                stack.append(int(token))
        
        # At the end, the stack has one element → the final result
        return stack.pop()
