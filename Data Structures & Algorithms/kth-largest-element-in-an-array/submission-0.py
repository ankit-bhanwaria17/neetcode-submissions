class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for n in nums:
            heapq.heappush(maxHeap, -1*n)
        while k > 1:
            heapq.heappop(maxHeap)
            k -= 1
        return heapq.heappop(maxHeap)*-1