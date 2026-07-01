class MinStack:

    def __init__(self):
        self.length = 0
        self.arr = []
        self.min_values = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.min_values:
            self.min_values.append(val)
        elif val <= self.min_values[-1]:
            self.min_values.append(val) 

    def pop(self) -> None:
        if self.arr[-1] == self.min_values[-1]:
            self.min_values.pop()
        del self.arr[-1]
        


    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min_values[-1]
