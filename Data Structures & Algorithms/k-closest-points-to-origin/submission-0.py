class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for p in points:
            d = math.sqrt(math.pow(p[0], 2) + math.pow(p[1], 2))
            dist.append((d, p))
        heapq.heapify(dist)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(dist)[1])
        return res