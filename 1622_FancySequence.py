class Fancy(object):

    def __init__(self):
        self.mod = 10**9 + 7          # modulo for large number operations
        self.val = []                 # stores normalized base values
        self.a = 1                    # global multiplier
        self.b = 0                    # global addition

    def append(self, val):
        """
        :type val: int
        :rtype: None
        """
        # reverse current transformation to store base value
        x = (val - self.b + self.mod) % self.mod
        
        # divide by 'a' using modular inverse of a
        self.val.append(x * pow(self.a, self.mod - 2, self.mod) % self.mod)

    def addAll(self, inc):
        """
        :type inc: int
        :rtype: None
        """
        # update global addition
        self.b = (self.b + inc) % self.mod

    def multAll(self, m):
        """
        :type m: int
        :rtype: None
        """
        # update global multiplier
        self.a = (self.a * m) % self.mod
        
        # addition must also scale after multiplication
        self.b = (self.b * m) % self.mod

    def getIndex(self, idx):
        """
        :type idx: int
        :rtype: int
        """
        if idx >= len(self.val):
            return -1   # index out of range
        
        # apply current transformation to stored base value
        return (self.a * self.val[idx] + self.b) % self.mod


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)