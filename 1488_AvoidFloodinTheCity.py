class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        import bisect  # used to keep dry days sorted and search efficiently
        
        n = len(rains)             # total number of days
        ans = [-1] * n             # final answer array
        full = {}                  # stores last day when each lake was filled
        dry_days = []              # stores indices of days when we can dry a lake
        
        for i, lake in enumerate(rains):  # go through each day
            if lake > 0:  # raining on some lake
                if lake in full:  # if this lake is already full
                    # find a dry day that comes after the last time this lake was filled
                    idx = bisect.bisect_right(dry_days, full[lake])
                    
                    # if no such dry day found → flood happens
                    if idx == len(dry_days):
                        return []
                    
                    # pick that dry day to dry this lake
                    dry_day = dry_days[idx]
                    ans[dry_day] = lake  # assign lake number to that dry day
                    
                    # remove that day since it’s now used
                    dry_days.pop(idx)
                
                # mark this lake as filled today
                full[lake] = i
            else:
                # if no rain, this is a dry day → store its index
                bisect.insort(dry_days, i)  # keep list sorted
                ans[i] = 1  # temporary value (will change later if used)
        
        return ans  # return final result
