class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []  # store numbers in lexicographical order
        curr = 1  # start from 1
        
        for i in range(n):
            res.append(curr)  # add current number to result
            
            # try to go deeper (like 1 -> 10)
            if curr * 10 <= n:
                curr *= 10
            # if cannot go deeper, move to next valid number
            else:
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10  # move one level up
                curr += 1  # move to next number
        
        return res  # return the lexicographical list
