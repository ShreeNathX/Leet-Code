class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        c = m = 0
        for i in gain:
            c += i
            m = max(c, m)
        return m