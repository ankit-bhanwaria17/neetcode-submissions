class MedianFinder:

    def __init__(self):
        self.minHeap = [] # 2nd half of list
        self.maxHeap = [] # 1st half of list
    
    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, -heapq.heappushpop(self.maxHeap, -num))
        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (-self.maxHeap[0] + self.minHeap[0])/2
        
        return float(-self.maxHeap[0])