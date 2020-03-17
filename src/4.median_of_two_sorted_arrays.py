from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.find_kth_min_solution(nums1, nums2)

    # 找第 m+n//2 小 解决方法
    def find_kth_min_solution(self, nums1, nums2):
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            nums1, nums2 = nums2, nums1
            len1, len2 = len2, len1

        i_kth_min = (len1 + len2 + 1) // 2
        cut1, cut2 = 0, 0  # 0 to length | nums[cut-1] is left | nums[cut] is right

        is_odd = bool((len1 + len2) & 1)

        while i_kth_min > 1:
            cut_num = i_kth_min // 2

            if cut1 == len1:
                cut2 += i_kth_min - 1
                break

            if cut1 + cut_num >= len1:
                tmp_cut1 = len1
                tmp_cut2 = cut1 + cut_num - len1 + cut_num + cut2

            else:
                tmp_cut1 = cut1 + cut_num
                tmp_cut2 = cut2 + cut_num

            if nums1[tmp_cut1 - 1] < nums2[tmp_cut2 - 1]:
                cut_len = tmp_cut1 - cut1
                cut1 = tmp_cut1
            else:
                cut_len = tmp_cut2 - cut2
                cut2 = tmp_cut2

            i_kth_min -= cut_len

        # cutNum == 0

        # 切完短列表的情况
        if cut1 == len1:
            midleft = nums2[cut2]
            cut2 += 1
        # 两个列表切点都在中间
        elif nums1[cut1] < nums2[cut2]:
            midleft = nums1[cut1]
            cut1 += 1
        else:
            midleft = nums2[cut2]
            cut2 += 1

        if is_odd:
            return float(midleft)

        if cut1 == len1:
            midright = nums2[cut2]
        elif cut2 == len2:
            midright = nums1[cut1]
        else:
            midright = min(nums1[cut1], nums2[cut2])
        return (midleft + midright) / 2

    # 切割法
    def cutting_solution(self, nums1, nums2):
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            nums1, nums2, len1, len2 = nums2, nums1, len2, len1

        if len2 == 0:
            return 0

        i_begin, i_end, half_len = 0, len1, (len1 + len2 + 1) // 2
        while i_begin <= i_end:
            i1 = (i_begin + i_end) // 2
            i2 = half_len - i1

            if i1 < len1 and nums1[i1] < nums2[i2 - 1]:
                # 提高索引下限
                i_begin = i1 + 1
            elif i1 > 0 and nums1[i1 - 1] > nums2[i2]:
                # 缩小上限
                i_end = i1 - 1
            else:

                if i1 == 0:
                    # 切处没有左侧了，中间值左侧那个值在另一个的列表中切处的左侧
                    max_left = nums2[i2 - 1]
                elif i2 == 0:
                    max_left = nums1[i1 - 1]
                else:
                    max_left = max(nums1[i1 - 1], nums2[i2 - 1])

                if (len1 + len2) & 1 == 1:
                    return max_left

                if i1 == len1:
                    # 同理，nums1切处没有右侧了，中间值右侧的值在另一个列表切处的右侧
                    min_right = nums2[i2]
                elif i2 == len2:
                    min_right = nums1[i1]
                else:
                    min_right = min(nums1[i1], nums2[i2])

                return (max_left + min_right) / 2
