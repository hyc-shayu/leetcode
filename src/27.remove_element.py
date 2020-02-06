from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        length = 0
        remove = 0

        for fast in range(len(nums)):
            if nums[fast] != val:
                length += 1
                if remove > 0:
                    nums[fast - remove] = nums[fast]
            else:
                remove += 1

        return length


if __name__ == '__main__':
    a = [3, 2, 2, 9, 7, 3]
    print(Solution().removeElement(a, 3))
    print(a)
