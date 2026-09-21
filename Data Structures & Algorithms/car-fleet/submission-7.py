class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carData = [[p, s] for p, s in zip(position, speed)]
        carData.sort(key=lambda x:-x[0])
        result = 0
        stack = []
        for p, s in carData:
            time = (target - p)/s
            if not stack:
                stack.append(time)
                continue

            if time > stack[-1]:
                stack.append(time)

        return len(stack)
