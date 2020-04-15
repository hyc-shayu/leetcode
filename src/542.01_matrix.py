from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """动态规划, 从左上角和右下角开始
        f(i, j) 的距离为 左边或上边的最小值+1
        f(i, j) = 1 + min(f(i-1, j), f(i, j-1))
        f(i, j) 的距离为 自己和 (右边和下边的最小值+1) 的最小值
        f(i, j) = min(f(i, j), 1 + min(f(i+1, j), f(i, j+1)))
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    continue
                left = right = 200
                if i - 1 >= 0:
                    left = matrix[i - 1][j] + 1
                if j - 1 >= 0:
                    right = matrix[i][j - 1] + 1
                matrix[i][j] = min(left, right)

        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[i]) - 1, -1, -1):
                if matrix[i][j] == 0:
                    continue
                if i + 1 < len(matrix):
                    matrix[i][j] = min(matrix[i][j], matrix[i + 1][j] + 1)
                if j + 1 < len(matrix[i]):
                    matrix[i][j] = min(matrix[i][j], matrix[i][j + 1] + 1)

        return matrix


if __name__ == '__main__':
    assert Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]) == [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
