class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """

        # totalDrunk keeps track of how many bottles we have drunk
        totalDrunk = 0

        # empty keeps track of how many empty bottles we have after drinking
        empty = 0

        # While we still have full bottles to drink
        while numBottles > 0:
            # Drink all available full bottles
            totalDrunk += numBottles

            # Those full bottles become empty bottles
            empty += numBottles

            # All full bottles are now drunk, so reset numBottles to 0
            numBottles = 0

            # If we have enough empty bottles to exchange for a new one
            if empty >= numExchange:
                # Spend numExchange empty bottles to get 1 full bottle
                empty -= numExchange

                # Now we have 1 new full bottle
                numBottles = 1

                # After each exchange, requirement increases by 1
                numExchange += 1

        # Return the total number of bottles we managed to drink
        return totalDrunk
