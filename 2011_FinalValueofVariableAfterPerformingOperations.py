class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0  # initialize X to 0
        for op in operations:  # loop through each operation
            if "++" in op:  # if operation contains increment
                x += 1  # increment X by 1
            else:  # otherwise, it's a decrement
                x -= 1  # decrement X by 1
        return x  # return final value of X
