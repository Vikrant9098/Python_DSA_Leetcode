class Solution:
    ALPHABET_SIZE = 26  # total letters in the English alphabet

    def maxPartitionsAfterOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == self.ALPHABET_SIZE:
            return 1  # if k=26, whole string is one partition (all letters allowed)

        n = len(s)  # length of string
        ansr = [0] * n  # stores partitions count from right to left
        usedr = [0] * n  # stores bitmask of used chars from right to left
        used = 0  # bitmask of current characters used
        cntUsed = 0  # number of distinct chars used in current segment
        ans = 1  # initial partition count

        # process from right to left
        for i in range(n - 1, -1, -1):
            ch = ord(s[i]) - ord('a')  # get current character index
            if (used & (1 << ch)) == 0:  # if char not used yet
                if cntUsed == k:  # if already k distinct chars used
                    cntUsed = 0  # reset distinct count
                    used = 0  # reset used bitmask
                    ans += 1  # start a new partition
                used |= (1 << ch)  # mark current char as used
                cntUsed += 1  # increase distinct char count
            ansr[i] = ans  # store current partition count from this index
            usedr[i] = used  # store used bitmask from this index

        ansl = 0  # partitions counted from left
        ans = ansr[0]  # start with partitions counted from right

        l = 0  # left pointer
        while l < n:
            used = 0  # bitmask of chars used in current left segment
            cntUsed = 0  # count of distinct chars in left segment
            usedBeforeLast = 0  # used chars before last new char
            usedTwiceBeforeLast = 0  # chars repeated before last new char
            last = -1  # index of last new char added
            r = l  # right pointer

            # expand window from left to right
            while r < n:
                ch = ord(s[r]) - ord('a')  # current char index
                if (used & (1 << ch)) == 0:  # if new char
                    if cntUsed == k:  # if limit reached
                        break  # stop expanding
                    usedBeforeLast = used  # store used before adding this char
                    last = r  # mark this as last added
                    used |= (1 << ch)  # add to used set
                    cntUsed += 1  # increment distinct count
                elif cntUsed < k:  # if not full, but char repeats
                    usedTwiceBeforeLast |= (1 << ch)  # mark as repeated
                r += 1  # move right

            # if exactly k distinct chars in current window
            if cntUsed == k:
                # check if changing one char before "last" gives more partitions
                if last - l > bin(usedBeforeLast).count('1'):
                    ans = max(ans, ansl + 1 + ansr[last])

                # check characters after the last one
                if last + 1 < r:
                    if last + 2 >= n:  # if near end of string
                        ans = max(ans, ansl + 1 + 1)
                    else:
                        # if next segment already has k distinct chars
                        if bin(usedr[last + 2]).count('1') == k:
                            # find if any unused char still available
                            canUse = ((1 << self.ALPHABET_SIZE) - 1) & ~used & ~usedr[last + 2]
                            if canUse > 0:
                                ans = max(ans, ansl + 1 + 1 + ansr[last + 2])
                            else:
                                ans = max(ans, ansl + 1 + ansr[last + 2])
                            l1 = ord(s[last + 1]) - ord('a')  # get next char
                            # if next char not repeated earlier
                            if (usedTwiceBeforeLast & (1 << l1)) == 0:
                                ans = max(ans, ansl + 1 + ansr[last + 1])
                        else:
                            ans = max(ans, ansl + 1 + ansr[last + 2])

            l = r  # move left pointer to next segment
            ansl += 1  # increment left-side partition count

        return ans  # return final max partitions
