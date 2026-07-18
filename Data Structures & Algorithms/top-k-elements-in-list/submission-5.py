class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        bucket = []
        for i in range(len(nums)+1):
            bucket.append([])
        for key, value in count.items():
            bucket[value].append(key)
        res = []
        for i in range(len(bucket)-1, 0, -1):
            if len(res) == k:
                break
            if bucket[i]:
                res.extend(bucket[i])
        return res