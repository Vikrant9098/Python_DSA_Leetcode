class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """

        # Store elements smaller than pivot
        less = []

        # Store elements equal to pivot
        equal = []

        # Store elements greater than pivot
        greater = []

        # Traverse through each element in the array
        for num in nums:

            # Place smaller elements into the 'less' list
            if num < pivot:
                less.append(num)

            # Place greater elements into the 'greater' list
            elif num > pivot:
                greater.append(num)

            # Place equal elements into the 'equal' list
            else:
                equal.append(num)

        # Append all pivot elements after smaller elements
        less.extend(equal)

        # Append all greater elements at the end
        less.extend(greater)

        # Return the rearranged array
        return less