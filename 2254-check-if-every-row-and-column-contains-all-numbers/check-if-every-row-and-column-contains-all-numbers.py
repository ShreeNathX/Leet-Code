class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        n = len(matrix)
        x = set(range(1, n+1))

        for i in range(n):
            if set(matrix[i]) != x:
                return False
        
        for j in range(n):
            col = [matrix[i][j] for i in range(n)]
            if set(col) != x:
                return False
        return True

        