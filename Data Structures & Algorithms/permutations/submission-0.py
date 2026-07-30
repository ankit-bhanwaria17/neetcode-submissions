class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visitedNums = [False for _ in range(len(nums))]
        self.result = []

        def dfs(visitedNums, currRes):
            if len(currRes) == len(nums):
                self.result.append(currRes[:])
                return
            
            for i in range(len(nums)):
                if visitedNums[i]:
                    continue
                visitedNums[i] = True
                currRes.append(nums[i])

                dfs(visitedNums, currRes)

                visitedNums[i] = False
                currRes.pop()

        dfs(visitedNums, [])
        return self.result