# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator          # store the original iterator
        self._has_next = iterator.hasNext()  # check if there is a next element
        self._next = iterator.next() if self._has_next else None  # store next element if exists

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next  # just return the stored next element

    def next(self):
        """
        :rtype: int
        """
        curr = self._next  # save the current element to return
        self._has_next = self.iterator.hasNext()  # check if more elements exist
        self._next = self.iterator.next() if self._has_next else None  # move iterator forward
        return curr  # return current element

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._has_next  # return whether more elements are available
