class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        memory = set()

        def compute(*args):
            res = 0
            for digit in args:
                while digit > 0:
                    res += digit % 10
                    digit //= 10
            return res

        def dfs(x, y):
            if x >= m or y >= n or (x, y) in memory:
                return 0
            memory.add((x, y))
            res = compute(x, y)
            if res > k:
                return 0
            return 1 + dfs(x + 1, y) + dfs(x, y + 1)

        return dfs(0, 0)


if __name__ == '__main__':
    sol = Solution()
    assert 15 == sol.movingCount(16, 8, 4)
