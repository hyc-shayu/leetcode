class Solution:
    def massage(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]

        result = {(0, 0): 0, (0, 1): nums[0]}
        for i in range(1, len(nums)):
            # f(n, 不取) = max(f(n-1, 不取), f(n-1, 取))
            result[(i, 0)] = max(result[(i - 1, 0)], result[(i - 1, 1)])
            # f(n, 取) = f(n-1, 不取) + nums[n]
            result[(i, 1)] = result[(i - 1, 0)] + nums[i]

        return max(result[len(nums) - 1, 0], result[len(nums) - 1, 1])
