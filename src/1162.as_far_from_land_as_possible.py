from typing import List
from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        n = len(grid)
        queue = deque()
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    queue.append((x, y))
        visited = set(queue)

        gap = '#'
        queue.append(gap)

        max_distance = 0
        found_ocean = False
        deep = 0

        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

        def append_neighbourhood(x_, y_):
            for i in range(4):
                x1, y1 = x_ + dx[i], y_ + dy[i]
                if 0 <= x1 < n and 0 <= y1 < n and (x1, y1) not in visited:
                    visited.add((x1, y1))
                    queue.append((x1, y1))

        # 多源bfs
        while queue:
            head = queue.popleft()
            if head == gap:
                if queue:
                    found_ocean = False
                    deep += 1
                    queue.append(gap)
                    continue
                else:
                    break
            x, y = head
            if not found_ocean and grid[x][y] == 0:
                found_ocean = True
                max_distance = deep
            append_neighbourhood(x, y)

        return max_distance if max_distance > 0 else -1


if __name__ == '__main__':
    assert Solution().maxDistance(
        [[1, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 1, 0, 1, 1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 0, 0, 1, 0, 0],
         [1, 0, 1, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
         [0, 0, 0, 1, 1, 1, 1, 0, 0, 1], [0, 1, 0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
         [1, 1, 0, 1, 1, 1, 1, 1, 0, 0]]) == 2
