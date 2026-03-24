class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = defaultdict(list)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                d[i+j].append(mat[i][j])

        result = []
        for k in range(len(mat) + len(mat[0]) - 1):
            if k % 2 == 0:
                result.extend(d[k][::-1])
            else:
                result.extend(d[k])
        return result