from collections import deque


class Solution:
    def numIslands(self, grid):
        # 使用一维数组要把二维索引计算转换成一维索引
        # 使用二维数组存储元组
        # 这里使用字典
        uf = dict()
        count = 0  # uf中的集合数量
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    uf[(i, j)] = (i, j)
                    # 初始化 每块陆地 都视为一个集合
                    count += 1

        def find_root(position):
            root = position
            while root != uf[root]:
                root = uf[root]
            # 路径压缩
            while uf[position] != root:
                position, uf[position] = uf[position], root
            return root

        def union(pos1, pos2):
            root1 = find_root(pos1)
            root2 = find_root(pos2)
            if root1 != root2:
                uf[root2] = root1
                # 合并后 count -= 1
                return - 1
            return 0

        # 只需向右下方的陆地合并即可
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '0':
                    continue
                if i + 1 < len(grid) and grid[i + 1][j] == '1':
                    count += union((i, j), (i + 1, j))
                if j + 1 < len(grid[i]) and grid[i][j + 1] == '1':
                    count += union((i, j), (i, j + 1))

        return count

    def numIslandsBFS(self, grid):
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()

        def is_valid(i, j):
            return (0 <= i < len(grid) and 0 <= j < len(grid[i]) and
                    grid[i][j] == '1' and (i, j) not in visited)

        def bfs(i, j):
            if is_valid(i, j):
                queue = deque([(i, j)])
                visited.add((i, j))
                while queue:
                    cur_i, cur_j = queue.popleft()
                    for di, dj in direction:
                        crd = (cur_i + di, cur_j + dj)
                        if is_valid(*crd):
                            visited.add(crd)
                            queue.append(crd)
                return 1
            return 0

        return sum(bfs(i, j) for i in range(len(grid)) for j in range(len(grid[i])))

    def numIslandsDFS(self, grid):
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                for _ in map(sink, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1)):
                    pass
                return 1
            return 0

        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))


if __name__ == '__main__':
    assert 1 == Solution().numIslands(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"],
         ["0", "0", "0", "0", "0"]])
