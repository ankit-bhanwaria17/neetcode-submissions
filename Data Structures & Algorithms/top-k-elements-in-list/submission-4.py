class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = defaultdict(int)
        for n in nums:
            numsDict[n] += 1
        bucket = [[] for i in range(len(nums)+1)]
        for num, count in numsDict.items():
            bucket[count].append(num)
        res = []
        for i in range(len(bucket)-1, 0, -1):
            res.extend(bucket[i])
            if len(res) == k:
                return res
        return res
