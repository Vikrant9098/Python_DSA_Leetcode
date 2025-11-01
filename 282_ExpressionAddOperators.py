class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []  # store all valid expressions

        # helper function for backtracking
        def backtrack(index, path, eval_val, prev_num):
            # if we reached the end of the string
            if index == len(num):
                # if total value equals target, add to result
                if eval_val == target:
                    res.append(path)
                return

            # try all possible splits of the remaining string
            for i in range(index, len(num)):
                # skip numbers with leading zeros
                if i != index and num[index] == '0':
                    break

                # take current substring as a number
                curr = int(num[index:i + 1])

                # if first number, it starts without an operator
                if index == 0:
                    backtrack(i + 1, path + str(curr), curr, curr)
                else:
                    # try '+'
                    backtrack(i + 1, path + '+' + str(curr), eval_val + curr, curr)

                    # try '-'
                    backtrack(i + 1, path + '-' + str(curr), eval_val - curr, -curr)

                    # try '*', adjust eval to respect precedence
                    backtrack(i + 1, path + '*' + str(curr), eval_val - prev_num + prev_num * curr, prev_num * curr)

        # start recursion from index 0
        backtrack(0, "", 0, 0)

        # return final result list
        return res
