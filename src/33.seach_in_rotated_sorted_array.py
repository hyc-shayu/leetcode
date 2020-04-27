from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        il, ir = 0, len(nums) - 1
        while il <= ir:
            mid = (il + ir) // 2
            if nums[mid] == target:
                return mid
            # 连续段在左侧 nums[il] < nums[mid] 或者 mid == il
            elif nums[mid] >= nums[il]:
                if nums[mid] > target >= nums[il]:
                    ir = mid - 1
                else:
                    il = mid + 1
            # 连续段在右侧 nums[mid] < nums[ir]
            else:
                if nums[ir] >= target > nums[mid]:
                    il = mid + 1
                else:
                    ir = mid - 1
        return -1


if __name__ == '__main__':
    assert 1 == Solution().search([3, 1], 1)
