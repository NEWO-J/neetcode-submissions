class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []
        if len(position) == 1:
            return 1

        for pos,speed in zip(position,speed):
            cars.append([pos,speed]) 

        sorted_cars = sorted(cars)

        for i in range(len(position) - 1, -1, -1):
            finish_time = (target - sorted_cars[i][0]) / sorted_cars[i][1]
            if stack and stack[-1] >= finish_time:
                continue
            else:
                stack.append(finish_time)
            

        return len(stack)
