class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        

        for s in tokens:
            
            if s not in "+-*/":
                stack.append(int(s))
            else:
                right = stack.pop()
                left = stack.pop()
                if s == "+":
                    result = left + right
                elif s == "-":
                    result = left - right
                elif s == "*":
                    result = left * right
                elif s == "/":
                    result = int(left/right)
                stack.append(result)
        return int(stack[0])
        