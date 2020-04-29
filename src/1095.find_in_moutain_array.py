# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """


class MountainArray:
    def __init__(self, array):
        self.array = array

    def get(self, index: int) -> int:
        return self.array[index]

    def length(self) -> int:
        return len(self.array)


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        if mountain_arr.length() < 1:
            return -1

        idx_l, idx_r = 0, mountain_arr.length() - 1
        left_val, right_val = mountain_arr.get(idx_l), mountain_arr.get(idx_r)
        result = []

        def binary_search(left, right):
            if left < right:
                cmp = lambda x, y: x > y
            else:
                cmp = lambda x, y: x < y
                left, right = right, left

            while left <= right:
                mid = (right + left) // 2
                mid_num = mountain_arr.get(mid)
                if mid_num == target:
                    result.append(mid)
                    return
                elif cmp(target, mid_num):
                    left = mid + 1
                else:
                    right = mid - 1

        while idx_l <= idx_r and len(result) < 2:
            idx_m = (idx_l + idx_r) // 2
            mid_val = mountain_arr.get(idx_m)
            # 左边是升序 山峰在 [idx_m, idx_r]                          idx_m == idx_l的情况
            if idx_m > idx_l and mountain_arr.get(idx_m - 1) < mid_val or (idx_m == idx_l and
                                                                           mid_val <= mountain_arr.get(idx_r)):
                # target在左侧 升序中
                if mid_val >= target >= left_val:
                    binary_search(idx_l, idx_m)
                idx_l = idx_m + 1
            # 右侧是降序
            else:
                # target 在右侧降序中
                if mid_val >= target >= right_val:
                    binary_search(idx_r, idx_m)
                idx_r = idx_m - 1

        return min(result) if result else -1


if __name__ == '__main__':
    arr = MountainArray([0, 5, 3, 1])
    print(Solution().findInMountainArray(1, arr))
