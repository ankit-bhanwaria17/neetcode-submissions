class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)] 
        cars.sort(reverse=True)
        fleet = 1
        stack = [(target - cars[0][0])/cars[0][1]]
        for i in range(1, len(cars)):
            time = (target - cars[i][0])/cars[i][1]
            if stack[-1] < time:
                fleet += 1
                stack = [time]
        return fleet
