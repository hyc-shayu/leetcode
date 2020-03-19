class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # x轴 不重叠的情况, 左界和右界相等也算不重叠
        if rec1[0] >= rec2[2] or rec1[2] <= rec2[0]:
            return False
        # y轴 不重叠的情况, 上界和下界相等也算不重叠
        if rec1[1] >= rec2[3] or rec1[3] <= rec2[1]:
            return False
        return True
