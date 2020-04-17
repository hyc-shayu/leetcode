from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        greed
        """
        max_distance = 0
        for i in range(len(nums)):
            if i > max_distance:
                break
            max_distance = max(max_distance, nums[i] + i)
            if max_distance >= len(nums) - 1:
                return True
        return False

    def canJumpDP(self, nums: List[int]) -> bool:
        """
        dp超时 o(n^2)
        dp[-1] = True
        dp[i] = dp[i+1] or ... or dp[i+nums[i]] # nums[i] > 0
        dp[i] = False                           # nums[i] == 0
        """
        if not nums:
            return False

        dp = [False] * (len(nums) - 1) + [True]

        for i in range(len(nums) - 1, -1, -1):
            for j in range(min(i + nums[i], len(nums) - 1), i, -1):
                if dp[j]:
                    dp[i] = dp[j]  # True
                    break

        return dp[0]
