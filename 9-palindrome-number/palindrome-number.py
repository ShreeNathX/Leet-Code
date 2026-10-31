class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        res = 0
        y = x

        while y != 0:
            rem = y % 10
            res = res * 10 + rem
            y //= 10
        
        return res == x