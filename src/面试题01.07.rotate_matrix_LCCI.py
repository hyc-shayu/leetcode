from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        direct_x = [1, 1, -1]
        n = len(matrix)
        start = 0
        end = n - 1
        deep = 0
        while start < end:
            cur_len = n - 1 - 2 * deep
            for i in range(start, end):
                x, y = deep, i
                x_step = cur_len - y + deep
                for dx in direct_x:
                    next_x = dx * x_step + x
                    next_y = x
                    matrix[x][y], matrix[next_x][next_y] = matrix[next_x][next_y], matrix[x][y]
                    x, y = next_x, next_y
                    x_step = cur_len - x_step
            deep += 1
            start += 1
            end -= 1


if __name__ == '__main__':
    solution = Solution()
    # mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    solution.rotate(mat)
    print(mat)
