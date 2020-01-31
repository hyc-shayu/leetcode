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

        for i1 in len(len_nums):
            if nums[i1] > 0:    # 第一个数大于零就可以结束了
                break

            if i1 > 0 and nums[i1] == nums[i1-1]:   # 去除重复
                continue

            iLeft = i1 + 1
            iRight = len_nums - 1

            while iLeft < iRight:
                Sum = nums[i1] + nums[iLeft] + nums[iRight]

                if Sum == 0:
                    result.append([nums[i1], nums[iLeft], nums[iRight]])

                    iLeft += 1
                    iRight -= 1
                    
                    # 去除重复解
                    while iLeft < iRight and nums[iLeft] == nums[iLeft - 1]:
                        iLeft += 1

                    while iLeft < iRight and nums[iRight] == nums[iRight + 1]:
                        iRight -= 1

                elif Sum < 0:
                    iLeft += 1
                else:
                    iRight -= 1

        return result
