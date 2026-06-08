class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ops = ["+", "-", "/", "*"]

        for token in tokens:
            if token not in ops:
                stk.append(token)
            else:
                if token == "+":
                    operand1 = stk.pop()
                    operand2 = stk.pop()
                    res = int(operand1) + int(operand2)
                    stk.append(str(res))
                elif token == "*":
                    operand1 = stk.pop()
                    operand2 = stk.pop()
                    res = int(operand1) * int(operand2)
                    stk.append(str(res))
                elif token == "-":
                    operand1 = stk.pop()
                    operand2 = stk.pop()
                    res = int(operand2) - int(operand1)
                    stk.append(str(res))
                else:
                    a = int(stk.pop())
                    b = int(stk.pop())
                    res = int(b / a)
                    stk.append(res)

                    
        
        return int(stk[-1])

