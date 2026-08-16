class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        
        total = 0
        i = 0
        while i < len(gas):
            for j in range(i, len(gas)):
                total += gas[j] - cost[j]
                if total < 0:
                    break
            if total >= 0:
                break

            total = 0
            i = j+1
        return i

            