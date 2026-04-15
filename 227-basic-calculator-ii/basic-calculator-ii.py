class Solution:
    def calculate(self, s: str) -> int:
        num, stack, sign = 0, [], "+"
        s += "+"
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-*/":
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack[-1] *= num
                elif sign == "/":
                    stack[-1] = int(stack[-1] / num)
                num, sign = 0, c
        return sum(stack)