from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        # 表面积 = 所有正方体面积 - 接触面积
        # area = 6*v - k*2
        # 求出k即可知道总面积
        # grid[x][y]增加的接触面积 = min(grid[x-1][y], grid[x][y]) * 2 + min(grid[x][y-1], grid[x][y]) * 2
        count_area = 0
        contact_area = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                v = grid[x][y]
                if v > 0:
                    count_area += 6 * v
                    x_cnt_area = min(grid[x - 1][y], grid[x][y]) * 2 if x >= 1 else 0
                    y_cnt_area = min(grid[x][y - 1], grid[x][y]) * 2 if y >= 1 else 0
                    contact_area += x_cnt_area + y_cnt_area + (v - 1) * 2
        return count_area - contact_area


if __name__ == '__main__':
    solution = Solution()
    assert solution.surfaceArea([[2]]) == 10
    assert solution.surfaceArea([[1, 2], [3, 4]]) == 34
