# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#     def isInteger(self):
#         """
#         @return True if this NestedInteger holds a single integer, rather than a nested list.
#         :rtype bool
#         """
#
#     def getInteger(self):
#         """
#         @return the single integer that this NestedInteger holds, if it holds a single integer
#         Return None if this NestedInteger holds a nested list
#         :rtype int
#         """
#
#     def getList(self):
#         """
#         @return the nested list that this NestedInteger holds, if it holds a nested list
#         Return None if this NestedInteger holds a single integer
#         :rtype List[NestedInteger]
#         """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.flat = []               # list to store all integers
        self.index = 0               # pointer to current index
        self.flatten(nestedList)     # flatten the nested list

    def flatten(self, nestedList):
        # helper function to flatten nested structure
        for ni in nestedList:               
            if ni.isInteger():               # if it holds a single integer
                self.flat.append(ni.getInteger())  # add to flat list
            else:                            # if it's a nested list
                self.flatten(ni.getList())   # call flatten again (recursion)

    def next(self):
        """
        :rtype: int
        """
        val = self.flat[self.index]  # get current value
        self.index += 1              # move to next position
        return val                   # return the value

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < len(self.flat)   # true if more elements left


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
