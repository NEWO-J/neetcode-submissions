class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+','-','*','/'])
        stack = []
        for i in tokens:
            if i in operators:
                operator = i
                if operator == "+":
                    int1 = stack.pop()
                    int2 = stack.pop()
                    stack.append(int1 + int2)
      
                elif operator  == "-":
                    int1 = stack.pop()
                    int2 = stack.pop()
                    stack.append(int2 - int1)

                elif operator  == "*":
                    int1 = stack.pop()
                    int2 = stack.pop()
                    stack.append(int1 * int2)

                else:
                    int1 = stack.pop()
                    int2 = stack.pop() # says pop from empty list
                    stack.append(int(int2 / int1))
            else:
                stack.append(int(i))

        return int(stack[0])