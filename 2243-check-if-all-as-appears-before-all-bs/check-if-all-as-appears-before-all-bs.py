class Solution:
    def checkString(self, s: str) -> bool:
        seenA = False
        seenB = False

        for c in s:
            if c == 'a':
                if not seenB:
                    seenA = True
                else:
                    return False
            else:
                seenB = True
        return True