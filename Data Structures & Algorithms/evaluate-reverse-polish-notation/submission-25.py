class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+','-','*','/'])
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])
        for i in tokens:
            if i in operators:
                operator = i
                if operator == "+":
                    int1 = stack.pop()
                    int2 = stack.pop()
                    stack.append(int(int1) + int(int2))
      
                elif operator  == "-":
                    int1 = stack.pop()
                    int2 = stack.pop()
                    stack.append(int(int2) - int(int1))

                elif operator  == "*":
                    int1 = stack.pop()
                    int2 = stack.pop()
                    stack.append(int(int1) * int(int2))

                else:
                    int1 = stack.pop()
                    int2 = stack.pop() # says pop from empty list
                    stack.append(int(int2) / int(int1))
            else:
                stack.append(i)

        return int(stack[0])