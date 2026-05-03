class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # If lengths are not equal, rotation is impossible
        if len(s) != len(goal):
            return False
        
        # Concatenate string with itself
        # This contains all possible rotations of s
        doubled_string = s + s
        
        # Check if goal exists as a substring in doubled_string
        # If yes, goal is a valid rotation of s
        return goal in doubled_string