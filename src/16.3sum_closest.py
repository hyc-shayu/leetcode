class Solution:
    def threeSumClosest(self, nums, target):
        len_nums = len(nums)

        if len_nums < 3:
            return 0

        # sort
        nums.sort()

        closest = 2**31 - 1
        result = None

        for i in range(len_nums-2):
            left = i + 1
            right = len_nums - 1

            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                curDis = abs(target - curSum)
                if curDis < closest:
                    result = curSum
                    closest = curDis

                if curSum < target:
                    left += 1
                elif curSum > target:
                    right -= 1
                else:
                    return result
        return result

if __name__ == "__main__":
    obj = Solution()
    result = obj.threeSumClosest([1, -1, 2, 4], 1)
    print(result)

