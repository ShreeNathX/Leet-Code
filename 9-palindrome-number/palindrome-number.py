class Solution:
    def isPalindrome(self, x: int) -> bool:
        if  x < 0:
            return False

        original = abs(x)
        res = 0
        while x != 0:
            rem = x % 10
            res = res * 10 + rem
            x //= 10
        
        if original != res:
            return False
        return True