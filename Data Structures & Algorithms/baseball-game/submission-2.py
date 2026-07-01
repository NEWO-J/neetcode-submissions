class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        result = 0
        for i in operations:
            match i:
                case "+":
                    num1 = record.pop()
                    num2 = record.pop()
                    record.append(num2)
                    record.append(num1)
                    record.append(num1 + num2)
                case "C":
                    record.pop()
                case "D":
                    num1 = record.pop()
                    record.append(num1)
                    record.append(num1 * 2)
                case _:
                    record.append(int(i))
        
        for i in record:
            result += int(i)
        
        return result