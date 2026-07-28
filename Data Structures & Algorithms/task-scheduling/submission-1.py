class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = Counter(tasks)
        maxHeap = [-c for c in taskCount.values()]
        heapq.heapify(maxHeap)

        t = 0
        q = deque()

        while q or maxHeap:
            t += 1
            if maxHeap:
                count = heapq.heappop(maxHeap)
                count += 1
                if count < 0:
                    q.append([count, t + n])
            else:
                t = q[0][1]

            if q and q[0][1] == t:
                heapq.heappush(maxHeap, q.popleft()[0])
        return t  