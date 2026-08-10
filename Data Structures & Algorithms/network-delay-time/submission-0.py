class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n+1)}
        for n1, n2, t in times:
            adj[n1].append([n2, t])
        minHeap = []
        heapq.heappush(minHeap, [0, k])
        visited = set()
        time = 0
        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            time = t1
            visited.add(n1)
            for n2, t2 in adj[n1]:
                if n2 in visited:
                    continue
                heapq.heappush(minHeap, [t1 + t2, n2])
        return time if len(visited) == n else -1