class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, freq in count.items():
            bucket[freq].append(n)
        result = []
        for i in range(len(bucket)-1, -1, -1):
            if len(result) >= k:
                break
            result.extend(bucket[i])
        return result