class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxheap = []
        output = []
        l = 0
        for r in range(len(nums)):
            heapq.heappush(maxheap, [-nums[r], r])
            windowSize = r-l+1
            if windowSize == k:
                output.append(-maxheap[0][0])
                l += 1
                while maxheap and maxheap[0][1] < l:
                    heapq.heappop(maxheap)
        return output
                