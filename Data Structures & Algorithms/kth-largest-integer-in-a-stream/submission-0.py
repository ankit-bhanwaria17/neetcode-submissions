class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [(-1)*n for n in nums]
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, (-1)*val)
        temp = []
        for i in range(0, self.k):
            temp.append(heapq.heappop(self.nums))
        for i in temp:
            heapq.heappush(self.nums, i)
        return (-1)*temp[self.k-1]

