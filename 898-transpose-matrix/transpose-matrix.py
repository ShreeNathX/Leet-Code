class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        t_matrix = [[0]*m for _ in range(n)]
        for row in range(m):
            for col in range(n):
                t_matrix[col][row] = matrix[row][col]
        return t_matrix