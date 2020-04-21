from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        even = [0]  # even[i] 表示 第i个奇数 右边有多少个偶数
        for num in nums:
            if num & 1 == 1:
                even.append(0)
            else:
                even[-1] += 1
        result = 0
        for i in range(k, len(even)):  # 从第k个奇数开计算
            # 左右偶数 可以 选择0-even个偶数 相组合 即左右 子数组有 (even1 + 1) * (even2 + 1) 种组合
            # result[i] = (even[i-k] + 1) * (even[i] + 1)
            result += (even[i - k] + 1) * (even[i] + 1)
        return result
