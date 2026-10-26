class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))


        cars = sorted(cars, reverse=True)

        for car in cars:
            time = -(-(target - car[0]) / car[1])
            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)

            
        return len(stack)