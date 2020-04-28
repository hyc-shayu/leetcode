from typing import List
from functools import reduce


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        all_xor = reduce(lambda x, y: x ^ y, nums)
        div = 1
        while div & all_xor == 0:
            div <<= 1
        a, b = 0, 0
        for num in nums:
            if num & div:
                a ^= num
            else:
                b ^= num
        return [a, b]
