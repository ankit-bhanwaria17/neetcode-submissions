class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(speed)):
            cars.append([position[i], speed[i]])
        cars.sort(key=lambda x: x[0], reverse=True)
        timeToReach = []
        for c in cars:
            time = (target-c[0])/c[1]
            timeToReach.append(time)
        res = 0
        fleet = []
        print(f"timeToReach: {timeToReach}")
        for t in timeToReach:
            if len(fleet) == 0:
                fleet.append(t)
            else:
                if fleet[-1] >= t:
                    fleet.append(fleet[-1])
                else:
                    res += 1
                    fleet = [t]
        if len(fleet) != 0:
            res += 1
        return res
