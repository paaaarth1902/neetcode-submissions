class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        jointList = [[p, s] for p, s in zip(position, speed)]
        # print(sorted(jointList))
        numberOfFleets = 0
        time = 0

        for p, s in sorted(jointList)[::-1]:
            currTime = (target - p) / s
            if time < currTime:
                numberOfFleets += 1
                time = currTime


        return numberOfFleets