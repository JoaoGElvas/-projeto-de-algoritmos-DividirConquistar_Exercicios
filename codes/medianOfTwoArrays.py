class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        total_len = m + n
        left = 0
        right = m

        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (total_len + 1) // 2 - partition1

            left_max1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
            right_min1 = float("inf") if partition1 == m else nums1[partition1]
            left_max2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
            right_min2 = float("inf") if partition2 == n else nums2[partition2]

            if left_max1 <= right_min2 and left_max2 <= right_min1:
                if total_len % 2 == 0:
                    return (max(left_max1, left_max2) + min(right_min1, right_min2)) / 2
                else:
                    return max(left_max1, left_max2)

            elif left_max1 > right_min2:
                right = partition1 - 1
            else:
                left = partition1 + 1

        raise ValueError("Input arrays are not sorted.")
