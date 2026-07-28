class TimeMap:

    def __init__(self):
        self.timelist = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timelist:
            self.timelist[key] = [[timestamp, value]]
        else:
            self.timelist[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timelist:
            timelist = self.timelist[key]
        else:
            return ""
        l = 0
        r = len(timelist) - 1

        while l < r:
            midpoint = (l + r) // 2

            if timestamp > timelist[midpoint][0]:
                l = midpoint + 1
            else:
                r = midpoint  
            
        if timelist[l][0] > timestamp:
            if timelist[l - 1][0] < timestamp:
                return timelist[l - 1][1]

            return ""
        return timelist[l][1]


