from typing import List
from functools import lru_cache


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # dp[i] 第i天到最后一天旅游花费
        # dp[i] = min(dp[i+1] + cost[0], dp[i+7] + cost[1], dp[i+30] + cost[2]) # i in days
        # dp[i] = dp[i+1] # i not in days 不要花钱
        if not days:
            return 0
        days_set = set(days)

        @lru_cache(None)
        def dp(i):
            if i > days[-1]:
                return 0
            elif i in days_set:
                return min(dp(i + 1) + costs[0], dp(i + 7) + costs[1], dp(i + 30) + costs[2])
            else:
                return dp(i + 1)

        return dp(1)


if __name__ == '__main__':
    assert Solution().mincostTickets([1, 3, 4, 8, 11, 31], [1, 3, 10]) == 6
