class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # Split version1 and version2 into parts using '.'
        v1 = version1.split('.')
        v2 = version2.split('.')

        # Find the maximum length between both lists
        n = max(len(v1), len(v2))

        # Loop through each revision index
        for i in range(n):
            # Convert current part of version1 to int, if missing use 0
            num1 = int(v1[i]) if i < len(v1) else 0
            # Convert current part of version2 to int, if missing use 0
            num2 = int(v2[i]) if i < len(v2) else 0

            # Compare the numbers
            if num1 < num2:
                return -1  # version1 is smaller
            elif num1 > num2:
                return 1   # version1 is larger

        # If all revisions are equal
        return 0
