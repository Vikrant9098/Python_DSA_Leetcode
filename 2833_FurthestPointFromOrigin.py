class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        # Count how many times 'R' appears (move right)
        right = moves.count("R")
        
        # Count how many times 'L' appears (move left)
        left = moves.count("L")
        
        # Count how many '_' (free moves) appear
        free = moves.count("_")
        
        # Net distance from origin without considering '_'
        # abs ensures we take maximum distance regardless of direction
        distance = abs(right - left)
        
        # Each '_' can be used to move in the direction that increases distance
        # So we add all free moves to maximize the distance
        return distance + free