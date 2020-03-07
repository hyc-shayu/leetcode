class Solution:
    def threeSum(self, nums):
        if not nums:
            return []
        if len(nums) < 3:
            return []

        nums.sort()
        result = []

        # 排序+双指针
        len_nums = len(nums)

        for i1 in range(len_nums):
            if nums[i1] > 0:    # 第一个数大于零就可以结束了
                break

            if i1 > 0 and nums[i1] == nums[i1-1]:   # 去除重复
                continue

            i_left = i1 + 1
            i_right = len_nums - 1

            while i_left < i_right:
                sum_ = nums[i1] + nums[i_left] + nums[i_right]

                if sum_ == 0:
                    result.append([nums[i1], nums[i_left], nums[i_right]])

                    i_left += 1
                    i_right -= 1
                    
                    # 去除重复解
                    while i_left < i_right and nums[i_left] == nums[i_left - 1]:
                        i_left += 1

                    while i_left < i_right and nums[i_right] == nums[i_right + 1]:
                        i_right -= 1

                elif sum_ < 0:
                    i_left += 1
                else:
                    i_right -= 1

        return result
