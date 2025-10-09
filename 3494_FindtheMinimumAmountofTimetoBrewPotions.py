class Solution(object):
    def minTime(self, skill, mana):
        """
        :type skill: List[int]
        :type mana: List[int]
        :rtype: int
        """
        n = len(skill)  # number of wizards
        m = len(mana)   # number of potions
        done = [0] * (n + 1)  # done[i] = time when wizard i finishes the current potion

        for j in range(m):  # loop through each potion
            for i in range(n):  # loop through each wizard
                # wizard i+1 finishes when both current wizard and previous wizard are ready
                done[i + 1] = max(done[i + 1], done[i]) + mana[j] * skill[i]
            
            # adjust timing for next potion to avoid overlapping
            for i in range(n - 1, 0, -1):
                done[i] = done[i + 1] - mana[j] * skill[i]
        
        return done[n]  # total time when last wizard finishes last potion
