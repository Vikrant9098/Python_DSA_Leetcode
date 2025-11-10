# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#     def __init__(self, value=None):
#         pass
#     def isInteger(self):
#         pass
#     def add(self, elem):
#         pass
#     def setInteger(self, value):
#         pass
#     def getInteger(self):
#         pass
#     def getList(self):
#         pass

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        # If the string is just a number (no '['), return it as an integer
        if s[0] != '[':
            return NestedInteger(int(s))
        
        # Stack to keep track of nested lists
        stack = []
        num = ''
        
        for ch in s:
            # If '[' found, start a new NestedInteger (new list)
            if ch == '[':
                stack.append(NestedInteger())
            
            # If digit or '-' found, add it to num string
            elif ch.isdigit() or ch == '-':
                num += ch
            
            # If ',' or ']' found, handle the number and close lists if needed
            elif ch in [',', ']']:
                # If we have a number, add it as a NestedInteger
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ''
                # If ']' found and more than one element in stack, pop and add to parent
                if ch == ']' and len(stack) > 1:
                    ni = stack.pop()
                    stack[-1].add(ni)
        
        # Return the final NestedInteger structure
        return stack[0]
