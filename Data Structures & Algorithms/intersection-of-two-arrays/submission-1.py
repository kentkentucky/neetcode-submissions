class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # sort both nums1 and nums2
        nums1.sort()
        nums2.sort()
        # create pointer for both nums1 and nums2
        i = j = 0
        # create empty array for intersection
        intersection = []
        # loop while pointers are in boundary
        while i < len(nums1) and j < len(nums2):
            # check if nums1[i] > nums2[j]
            if nums1[i] > nums2[j] or nums2[j] in intersection:
                # increment j
                j += 1
            # check if nums2[j] > nums1[i]
            elif nums2[j] > nums1[i] or nums1[i] in intersection:
                # increment i
                i += 1
            else:
                # append element
                intersection.append(nums1[i])
        # return intersection
        return intersection
