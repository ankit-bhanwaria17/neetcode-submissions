class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.result = []
        def dfs(subset, start, total):
            if total == target:
                self.result.append(subset[:])
                return
            
            for i in range(start, len(candidates)):
                if total + candidates[i] > target:
                    return
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                subset.append(candidates[i])
                dfs(subset, i+1, total + candidates[i])
                subset.pop()
        
        dfs([], 0, 0)
        return self.result
