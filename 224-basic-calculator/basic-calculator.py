class Solution:
    def calculate(self, s: str) -> int:
        stack, num, sign, res = [], 0, 1, 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-":
                res += sign * num
                num, sign = 0, 1 if c == "+" else -1
            elif c == '(':
                stack.append((res, sign))
                res, sign = 0, 1
            elif c == ')':
                res += sign * num
                num = 0
                prev_res, prev_sign = stack.pop()
                res = prev_res + prev_sign * res
        return res + sign * num