class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()  # sort the first list
        nums2.sort()  # sort the second list
        
        i, j = 0, 0  # pointers for both lists
        result = []  # list to store common elements
        
        # loop until one list ends
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1  # move pointer i if nums1[i] is smaller
            elif nums1[i] > nums2[j]:
                j += 1  # move pointer j if nums2[j] is smaller
            else:
                result.append(nums1[i])  # add common element to result
                i += 1  # move both pointers forward
                j += 1
                
        return result  # return list of common elements
