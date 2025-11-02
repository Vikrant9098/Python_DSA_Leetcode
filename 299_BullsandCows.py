class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # count bulls
        bulls = 0
        # array to track digits seen (0–9)
        count = [0] * 10
        # count cows
        cows = 0

        # loop through each digit
        for i in range(len(secret)):
            s = secret[i]  # current digit in secret
            g = guess[i]   # current digit in guess

            # if both digits match → bull
            if s == g:
                bulls += 1
            else:
                sNum = int(s)  # convert secret char to number
                gNum = int(g)  # convert guess char to number

                # if guess digit was seen before in secret → cow
                if count[sNum] < 0:
                    cows += 1

                # if secret digit was seen before in guess → cow
                if count[gNum] > 0:
                    cows += 1

                # update counts for both digits
                count[sNum] += 1
                count[gNum] -= 1

        # return result in "xAyB" format
        return str(bulls) + "A" + str(cows) + "B"
