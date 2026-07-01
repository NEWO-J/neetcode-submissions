class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = [int(tokens[0])]
        for i in range(len(tokens)):
            if i == 0:
                continue
            match tokens[i]:
                case "+":
                    num1 = result.pop()
                    num2 = result.pop()
                    result.append(num1 + num2)
                case "-":
                    num1 = result.pop()
                    num2 = result.pop()
                    result.append(num2 - num1)
                case "/":
                    num1 = result.pop()
                    num2 = result.pop()
                    result.append(int(num2 / num1))
                case "*":
                    num1 = result.pop()
                    num2 = result.pop()
                    result.append(num1 * num2)
                case _:
                    result.append(int(tokens[i]))
        return(int(result[0]))