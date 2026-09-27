import heapq


class MedianFinder:
    def __init__(self):
        self.minHeap = []  # Larger half
        self.maxHeap = []  # Smaller half, stored as negative numbers

    def addNum(self, num: int) -> None:
        # Move the largest value from the smaller half to the larger half.
        largestLower = -heapq.heappushpop(self.maxHeap, -num)
        heapq.heappush(self.minHeap, largestLower)

        # Keep the smaller half the same size or one element larger.
        if len(self.minHeap) > len(self.maxHeap):
            smallestUpper = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -smallestUpper)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2

        return float(-self.maxHeap[0])