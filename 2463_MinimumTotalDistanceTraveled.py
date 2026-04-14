class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        # Sort robots and factories based on positions
        robot.sort()
        factory.sort()

        # Expand factory positions based on capacity
        factory_positions = []
        for f in factory:
            for i in range(f[1]):
                factory_positions.append(f[0])  # repeat position as per capacity

        # Start recursion from first robot and first factory
        return self._calculate_min_distance(0, 0, robot, factory_positions)

    def _calculate_min_distance(self, robot_idx, factory_idx, robot, factory_positions):
        # If all robots are assigned, no more distance needed
        if robot_idx == len(robot):
            return 0

        # If no factories left but robots remain → invalid case
        if factory_idx == len(factory_positions):
            return 1e12  # large number to avoid choosing this path

        # Option 1: Assign current robot to current factory
        assign = abs(robot[robot_idx] - factory_positions[factory_idx]) + \
                 self._calculate_min_distance(robot_idx + 1, factory_idx + 1, robot, factory_positions)

        # Option 2: Skip current factory position
        skip = self._calculate_min_distance(robot_idx, factory_idx + 1, robot, factory_positions)

        # Return minimum of both choices
        return min(assign, skip)