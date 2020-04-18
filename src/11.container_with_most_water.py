from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        # 面积被限制在短的那边 只有短的向中间移动到变长了,才有可能超过原来的面积
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            # 简化循环
            if height[left] < height[right]:
                max_height = height[left]
                while left < right and max_height >= height[left]:
                    left += 1
            else:
                max_height = height[right]
                while left < right and max_height >= height[right]:
                    right -= 1

            # if height[left] < height[right]:
            #     next_left = left + 1
            #     while next_left < right:
            #         if height[next_left] > height[left]:
            #             break
            #         next_left += 1
            #     left = next_left
            # else:
            #     next_right = right - 1
            #     while left < next_right:
            #         if height[next_right] > height[right]:
            #             break
            #         next_right -= 1
            #     right = next_right

        return max_area


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
