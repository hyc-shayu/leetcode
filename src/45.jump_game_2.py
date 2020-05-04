from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # 能达到的最远距离
        max_pos = 0
        # 当前步数内能达到的最远距离
        end = 0
        # 步数
        step = 0
        for i in range(n-1):
            if end >= i:
                max_pos = max(max_pos, i + nums[i])
                if i == end:
                    end = max_pos
                    step += 1
        return step if end >= n - 1 else -1

    def jump_dp(self, nums):
        # O(n^2) 超时
        if not nums:
            return -1
        # dp[i] 表示到 i 最少需要几步
        # dp[i + nums[i]] = min(dp[i] + 1, dp[i + nums[i]])
        dp = [2**32 - 1] * len(nums)
        dp[0] = 0
        for i in range(0, len(nums)):
            for step in range(1, min(len(nums)-i, nums[i] + 1)):
                dp[i + step] = min(dp[i] + 1, dp[i + step])
        return dp[-1]


if __name__ == '__main__':
    assert 2 == Solution().jump_dp([2, 3, 1, 1, 4])
