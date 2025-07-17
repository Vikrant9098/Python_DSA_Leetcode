from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        # Queues to hold indices of 'R' and 'D' senators
        radiant = deque()
        dire = deque()
        
        n = len(senate)

        # Step 1: Store the indices of Radiant and Dire senators
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        # Step 2: Start the round-based banning process
        while radiant and dire:
            r_index = radiant.popleft()
            d_index = dire.popleft()

            # Whoever has the smaller index bans the other and comes back in the next round
            if r_index < d_index:
                radiant.append(r_index + n)
            else:
                dire.append(d_index + n)

        # Step 3: Declare the winner
        return "Radiant" if radiant else "Dire"
