class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
 
        output = 0
        cars = []
        stack = []
        if len(position) == 1:
            return 1

        for pos,speed in zip(position,speed):
            cars.append([pos,speed]) 
            output += 1

        sorted_cars = sorted(cars)

        for i in range(len(position) - 1, -1, -1):
            finish_time = (target - sorted_cars[i][0]) / sorted_cars[i][1]
            if stack and stack[-1] >= finish_time:
                output -= 1  
                # But if we pop before even adding our new value, we are deleting our
            else:
                stack.append(finish_time)
            

        return output
