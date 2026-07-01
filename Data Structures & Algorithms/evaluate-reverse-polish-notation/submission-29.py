class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+','-','*','/'])
        stack = []
        for i in tokens:
            if i in operators:
                operator = i
                if operator == "+":
                    int2 = stack.pop()
                    int1 = stack.pop()
                    stack.append(int1 + int2)
      
                elif operator  == "-":
                    int2 = stack.pop()
                    int1 = stack.pop()
                    stack.append(int1 - int2)

                elif operator  == "*":
                    int2 = stack.pop()
                    int1 = stack.pop()
                    stack.append(int1 * int2)

                else:
                    int2 = stack.pop()
                    int1 = stack.pop() # says pop from empty list
                    stack.append(int(int1 / int2))
            else:
                stack.append(int(i))

        return int(stack[0])