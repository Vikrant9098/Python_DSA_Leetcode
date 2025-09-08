class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_gas = 0       # Total gas available across all stations
        total_cost = 0      # Total cost to travel across all stations
        tank = 0            # Current gas in tank while traversing
        start = 0           # Candidate starting station index

        # Loop through all stations
        for i in range(len(gas)):
            total_gas += gas[i]         # Add gas at station i
            total_cost += cost[i]       # Add cost to go to next station

            tank += gas[i] - cost[i]    # Update current tank

            # If tank becomes negative, previous start is not valid
            if tank < 0:
                start = i + 1  # Try next station as starting point
                tank = 0       # Reset tank for next candidate

        # If total gas >= total cost, return the starting index; otherwise, -1
        return start if total_gas >= total_cost else -1
