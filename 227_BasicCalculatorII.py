class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []  # to store numbers
        num = 0     # current number
        op = '+'    # previous operator, start with '+'

        for i, c in enumerate(s):
            if c.isdigit():  # build the number
                num = num * 10 + int(c)
            
            # if operator or last char, process based on last operator
            if (not c.isdigit() and c != ' ') or i == len(s) - 1:
                if op == '+':
                    stack.append(num)  # push number
                elif op == '-':
                    stack.append(-num)  # push negative number
                elif op == '*':
                    stack.append(stack.pop() * num)  # multiply top with current
                elif op == '/':
                    top = stack.pop()
                    # truncate toward zero for division
                    stack.append(int(top / float(num)))
                
                op = c  # update operator
                num = 0  # reset number

        return sum(stack)  # sum all numbers for final result
