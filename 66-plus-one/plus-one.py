class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        val =  int("".join(map(str, digits)))
        val += 1
        return list(map(int, str(val)))