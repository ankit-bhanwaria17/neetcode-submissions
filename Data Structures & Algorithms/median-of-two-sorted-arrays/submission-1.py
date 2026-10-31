
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        # Binary search on the smaller array
        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1
        total = len(A) + len(B)
        half = total // 2  # Left half size; right gets extra if odd

        while True:
            # i, j = last indices of the left partitions
            i = l + (r - l) // 2
            j = half - i - 2  # (i+1) + (j+1) = half

            # Elements immediately around both partitions
            AL = A[i] if i >= 0 else float('-inf')
            AR = A[i+1] if i+1 < len(A) else float('inf')
            BL = B[j] if j >= 0 else float('-inf')
            BR = B[j+1] if j+1 < len(B) else float('inf')

            if AL > BR:
                r = i - 1  # Too many elements from A on left
            elif BL > AR:
                l = i + 1  # Too few elements from A on left
            else:
                # Valid partition: AL <= BR and BL <= AR
                if total % 2 == 0:
                    # Even: average of two middle elements
                    return (max(AL, BL) + min(AR, BR)) / 2
                else:
                    # Odd: smallest element on right
                    return min(AR, BR)
