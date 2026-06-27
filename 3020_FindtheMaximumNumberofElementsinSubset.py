from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Count the frequency of each number
        cnt = Counter(nums)

        # Frequency of 1 (0 if absent)
        one_cnt = cnt.get(1, 0)

        # Maximum odd count of 1's
        ans = one_cnt if one_cnt % 2 else one_cnt - 1

        # 1 is handled separately
        cnt.pop(1, None)

        # Try every remaining number as the starting point
        for num in cnt:
            res = 0
            x = num

            # Extend the chain while the current value appears at least twice
            while x in cnt and cnt[x] > 1:
                res += 2          # Pair contributes two elements
                x *= x            # Move to the next squared value

            # Add the center element if it exists, otherwise remove one excess count
            ans = max(ans, res + (1 if x in cnt else -1))

        return ans