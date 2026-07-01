class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        seconds_to_finish = []

        for i in range(len(speed)):
            position[i] = (position[i], speed[i])

        position = sorted(position, reverse=True)
        print(position)
        for pos in position:
            total = pos[0]
            seconds = (target - pos[0]) / pos[1]
            
            if not seconds_to_finish:
                seconds_to_finish.append(seconds)
            elif seconds > seconds_to_finish[-1]:
                seconds_to_finish.append(seconds)
 
        
        return len(seconds_to_finish)
