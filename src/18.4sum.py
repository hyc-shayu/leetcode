class Solution:
    def fourSum(self, nums, target):
        result = []
        if len(nums) < 4:
            return result

        nums.sort()

        i1 = 0
        while i1 < len(nums) - 3:
            i2 = i1 + 1
            while i2 < len(nums) - 2:
                # 比左右指针循环每次判断要快
                if not (nums[i1] + nums[i2] + nums[i2 + 1] + nums[i2 + 2] > target
                        or nums[i1] + nums[i2] + nums[-2] + nums[-1] < target):

                    left = i2 + 1
                    right = len(nums) - 1

                    while left < right:
                        tmp_sum = nums[i1] + nums[i2] + nums[left] + nums[right]
                        if tmp_sum == target:
                            result.append([nums[i1], nums[i2], nums[left], nums[right]])
                            left += 1
                            right -= 1

                        elif tmp_sum > target:
                            # 剪枝 如果target不在左右指针的区间内，不需要再移动指针了，直接跳出循环
                            # if nums[i1] + nums[i2] + nums[right] + nums[right - 1] < target:
                            #     break
                            right -= 1

                        else:
                            # if nums[i1] + nums[i2] + nums[left] + nums[left + 1] > target:
                            #     break
                            left += 1

                        if left > i2 + 1:
                            while left < right and nums[left] == nums[left - 1]:
                                left += 1
                        if right < len(nums) - 1:
                            while left < right and nums[right] == nums[right + 1]:
                                right -= 1

                i2 += 1
                while i2 < len(nums) - 2 and nums[i2] == nums[i2 - 1]:
                    i2 += 1

            i1 += 1
            if i1 < len(nums) - 3 and nums[i1] + nums[i1 + 1] + nums[i1 + 2] + nums[i1 + 3] > target:
                break

            while (i1 < len(nums) - 3 and (nums[i1] + nums[-3] + nums[-1] + nums[-2] < target
                                           or nums[i1] == nums[i1 - 1])):
                i1 += 1

        return result


if __name__ == '__main__':
    s = Solution()
    # result1 = s.fourSum([0, 1, 5, 0, 1, 5, 5, -4], 11)
    result1 = s.fourSum([-1, 0, 1, 2, -1, -4], -1)
    print(result1)
