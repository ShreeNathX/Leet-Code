class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        ans = 0
        n = len(mat)
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:
                    ans += mat[i][j]
        return ans