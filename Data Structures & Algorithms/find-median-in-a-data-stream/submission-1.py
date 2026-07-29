class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)
    
    def addNum(self, num: int) -> None:
        if not self.minHeap or num >= self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        
        diff = len(self.minHeap) - len(self.maxHeap)
        if diff > 0:
            numsToMove = diff // 2
            while numsToMove > 0:
                n = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -n)
                numsToMove -= 1
        if diff < 0:
            numsToMove = math.ceil(abs(diff/2))
            while numsToMove > 0:
                n = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, -n)
                numsToMove -= 1

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (-self.maxHeap[0] + self.minHeap[0])/2
        
        return float(self.minHeap[0])