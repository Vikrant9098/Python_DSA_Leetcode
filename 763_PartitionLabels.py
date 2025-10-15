class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        result = []  # list to store sizes of partitions
        last_index = {c: i for i, c in enumerate(s)}  # store last occurrence of each character

        start = 0  # start index of current partition
        end = 0    # end index of current partition

        for i, c in enumerate(s):  # iterate through the string
            end = max(end, last_index[c])  # extend end to last occurrence of current char
            if i == end:  # current index reaches end of partition
                result.append(end - start + 1)  # add partition size
                start = i + 1  # start next partition

        return result  # return list of partition sizes
