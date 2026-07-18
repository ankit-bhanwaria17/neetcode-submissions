class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        dq = deque() # index of nums
        l, r = 0, 0
        while r < len(nums):
            windowLen = r - l + 1
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)
            if windowLen < k:
                r += 1
                continue
            if windowLen == k:
                output.append(nums[dq[0]])
                r += 1
                l += 1
                while dq and dq[0] < l:
                    dq.popleft()
        return output