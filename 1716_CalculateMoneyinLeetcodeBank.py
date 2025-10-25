class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0  # total money saved
        week = n // 7  # number of complete weeks
        days = n % 7   # remaining days

        # Add money for complete weeks
        for i in range(week):
            total += 7 * (1 + i) + 21  # 21 = sum of 0 to 6

        # Add money for remaining days
        for i in range(days):
            total += (week + 1) + i  # Monday of this week starts from week+1

        return total
