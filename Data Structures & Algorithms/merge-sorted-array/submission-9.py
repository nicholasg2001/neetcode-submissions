class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # m = num valid elements in nums1 (cannot replace)
        # n = num elements in nums2 (need to add to nums1 in sorted order)
        # m = 4, n = 2
        # [10, 20, 20, 40, 0, 0]
        #  L                  R
        # [1, 2]

        for i in range(m, len(nums1)):
            nums1[i] = nums2[i-m]

        nums1.sort()

        