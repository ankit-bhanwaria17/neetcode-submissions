class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [(-1)*s for s in stones]
        heapq.heapify(minHeap)
        while len(minHeap) > 1:
            s1 = heapq.heappop(minHeap)
            s2 = heapq.heappop(minHeap)
            heapq.heappush(minHeap, abs(s1 - s2)*(-1))
        return minHeap[0]*(-1)