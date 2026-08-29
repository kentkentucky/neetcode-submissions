class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # initialise two pointers for nums1 and nums2
        # working backwards
        i = m - 1
        j = n - 1
        # initialise pointer for modification of nums1
        k = m + n - 1
        # while pointer is more than or equal 0
        while j >= 0:
            # check if nums1[i] is more than nums2[j]
            if i >= 0 and nums1[i] > nums2[j]:
                # assign index k to element nums1[i]
                nums1[k] = nums1[i]
                # decrement i
                i -= 1
            else:
                # assign index k to element nums2[j]
                nums1[k] = nums2[j]
                # decrement j
                j -= 1
            # decrement k
            k -= 1

                