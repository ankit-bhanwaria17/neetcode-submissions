class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        bucket = [[] for _ in range(len(nums)+1)]
        for key, value in count.items():
            bucket[value].append(key)
        result = []
        for i in range(len(bucket)-1, -1, -1):
            if len(result) >= k:
                break
            result.extend(bucket[i])
        return result
    