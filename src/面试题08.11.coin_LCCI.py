class Solution:
    def waysToChange(self, n: int) -> int:
        # f[i] = f[i-1] * f[1] + f[i-5] * f[5] + f[i-10] * f[10] + f[i-25] * f[25]
        # 错误 dp[6-1] * dp[1] + dp[6-5] * dp[5]
        #       2 * 1 + 1 * 2 = 4
        # dp[i][v] 前 i 种硬币 组成 v面值 的种数
        # dp[i][v] = dp[i - 1][v] + dp[i][v-c] c 为当前面值

        coin = (1, 5, 10, 25)
        dp = [0] * (n + 1)
        dp[0] = 1
        for c in coin:
            for i in range(c, n + 1):
                # dp[i][v] = dp[i-1][v] + dp[i][v - coin_i]
                dp[i] = dp[i] + dp[i - c]

        return dp[n] % 1000000007


if __name__ == '__main__':
    print(Solution().waysToChange(5))
    print(Solution().waysToChange(6))
    print(Solution().waysToChange(10))
