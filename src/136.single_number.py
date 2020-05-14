from typing import List
# from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # return reduce(lambda x, y: x ^ y, nums)
        res = 0
        for num in nums:
            res ^= num
        return res
