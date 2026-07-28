class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for t in tasks:
            count[t] = count.get(t, 0) + 1
        maxHeap = [] # [count, task]
        for key, value in count.items():
            heapq.heappush(maxHeap, [-value, key])
        time = 0
        q = deque() # [count, task, time]
        res = []
        while q or maxHeap:
            time += 1
            if maxHeap:
                count, task = heapq.heappop(maxHeap)
                res.append(task)
                count = count + 1
                if count < 0:
                    q.append([count, task, time + n])
            else:
                res.append("idle")

            if q and q[0][2] == time:
                    count, task, _ = q.popleft()
                    heapq.heappush(maxHeap, [count, task])

        return len(res)