from typing import List


class Solution:
    def majorityElement1(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for key in dic:
            if dic[key] > len(nums) / 2:
                return key
        return 0

    # Boyer-Moore
    def majorityElement(self, nums: List[int]) -> int:
        cur_num = 0
        count = 0
        for num in nums:
            if count == 0:
                cur_num = num
                count += 1
            elif cur_num == num:
                count += 1
            else:
                count -= 1
        return cur_num
