from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = deque()

        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)

        for car in cars:
            time = (target - car[0]) / car[1]
            if len(fleets) == 0 or fleets[-1] < time:
                fleets.append(time)
        
        return len(fleets)