from typing import List


class Solution:
    def permute(self, nums):
        """官方解法, 交换元素, 可以理解为谁排第一, 剩下的谁又第一"""
        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res

    def permute_(self, nums: List[int]) -> List[List[int]]:
        s_nums = set(nums)
        result = []
        res = []

        def recall():
            if not s_nums:
                result.append(res[:])
                return
            for num in list(s_nums):
                s_nums.remove(num)
                res.append(num)
                recall()
                res.pop()
                s_nums.add(num)

        recall()
        return result


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
