class Solution(object):
    def isSelfCrossing(self, distance):
        """
        :type distance: List[int]
        :rtype: bool
        """
        n = len(distance)  # get total number of moves

        # start checking from the 4th move, because before that no crossing can happen
        for i in range(3, n):
            
            # case 1: current line crosses the line 3 steps before
            if distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]:
                return True  # path crosses itself here

            # case 2: current line overlaps with the line 4 steps before
            if i >= 4 and distance[i - 1] == distance[i - 3] and \
               distance[i] + distance[i - 4] >= distance[i - 2]:
                return True  # path overlaps itself here

            # case 3: current line crosses the line 5 steps before
            if i >= 5 and distance[i - 2] >= distance[i - 4] and \
               distance[i - 1] <= distance[i - 3] and \
               distance[i - 1] + distance[i - 5] >= distance[i - 3] and \
               distance[i] + distance[i - 4] >= distance[i - 2]:
                return True  # path crosses again here

        return False  # if no crossing found, return False
