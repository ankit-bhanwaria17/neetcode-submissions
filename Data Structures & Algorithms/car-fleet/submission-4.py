class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carData = [(position[i], speed[i]) for i in range(len(speed))]
        carData.sort(key=lambda x:x[0])
        timeToReach = [(target-carData[i][0])/carData[i][1] for i in range(len(carData))]
        stack = []
        res = 0
        print(timeToReach)
        for i in range(len(timeToReach)-1, -1, -1):
            if stack and stack[0] >= timeToReach[i]:
                stack.append(timeToReach[i])
                continue
            stack = [timeToReach[i]]
            res += 1
        return res
