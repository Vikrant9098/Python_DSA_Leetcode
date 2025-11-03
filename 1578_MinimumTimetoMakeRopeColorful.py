class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        total_time = 0   # total time to remove balloons
        i = 0

        # loop through each balloon
        while i < len(colors) - 1:
            # if two consecutive balloons have same color
            if colors[i] == colors[i + 1]:
                # remove the one which takes less time
                if neededTime[i] < neededTime[i + 1]:
                    total_time += neededTime[i]   # add smaller time
                else:
                    total_time += neededTime[i + 1]
                    # swap so next comparison works correctly
                    neededTime[i + 1] = neededTime[i]
            i += 1

        return total_time
