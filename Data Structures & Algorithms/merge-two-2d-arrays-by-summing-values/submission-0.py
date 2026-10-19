class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        pass
        # initialise merged to an empty array
        merged = []
        # initialise two pointers to 0
        i = j = 0
        # loop through the arrays while in bound
        while i < len(nums1) and j < len(nums2):
            # get the id and value of i and j
            id1, value1 = nums1[i]
            id2, value2 = nums2[j]
            # check for matching id
            if id1 == id2:
                # append id and sum into merged
                merged.append([id1, value1 + value2])
                # increment i and j
                i += 1
                j += 1
            elif id1 < id2:
                # append id and value to merged
                merged.append(nums1[i])
                # increment i
                i += 1
            else:
                # append id and value to merged
                merged.append(nums2[j])
                # increment j
                j += 1

        # add remainder
        merged = merged + nums1[i:] + nums2[j:]

        # return merged
        return merged