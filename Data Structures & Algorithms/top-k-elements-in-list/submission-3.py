class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = defaultdict(int)
        for n in nums:
            numsDict[n] += 1
        bucket = []
        for i in range(len(nums)+2):
            bucket.append([])
        for num, count in numsDict.items():
            bucket[count].append(num)
        res = []
        for i in range(len(bucket)-1, 0, -1):
            if len(bucket[i]) == 0:
                continue
            res.extend(bucket[i])
            if len(res) == k:
                return res
        return res
