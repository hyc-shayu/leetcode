from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] 以i结尾的子序最大值
        # dp[i] = dp[i-1] + nums[i] if dp[i-1] > 0 else 0
        if not nums:
            return 0
        dp = [nums[0]]
        max_res = dp[0]
        for i in range(1, len(nums)):
            dp.append(dp[i - 1] + nums[i] if dp[i - 1] > 0 else nums[i])
            max_res = max(max_res, dp[-1])
        return max_res
