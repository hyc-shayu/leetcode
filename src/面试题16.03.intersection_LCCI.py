from typing import List


class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        x1, y1 = start1
        x2, y2 = end1
        x3, y3 = start2
        x4, y4 = end2

        def is_inside(x_1, x_2, x):
            """判断x是否在 x_1 - x_2 内"""
            x_1, x_2 = (x_1, x_2) if x_2 >= x_1 else (x_2, x_1)
            return x_1 <= x <= x_2

        def is_range_intersection():
            """两条线段的x轴范围和y轴范围是否都有相交"""
            # x3, x4 是否有一个在 x1-x2 范围内 y3, y4 是否 有一个在 y1-y2内
            x_1, x_2, x_3, x_4 = (x1, x2, x3, x4) if abs(x2 - x1) >= abs(x4 - x3) else (x3, x4, x1, x2)
            y_1, y_2, y_3, y_4 = (y1, y2, y3, y4) if abs(y2 - y1) >= abs(y4 - y3) else (y3, y4, y1, y2)
            return (is_inside(x_1, x_2, x_3) or is_inside(x_1, x_2, x_4)) and (
                    is_inside(y_1, y_2, y_3) or is_inside(y_1, y_2, y_4))

        if not is_range_intersection():
            return []

        # k = (y2 - y1) / (x2 - x1)   if x2 != x1
        # y1 = k * x1 + b
        # y2 = k * x2 + b
        # b = y1 - k * x1
        k1 = (y2 - y1) / (x2 - x1) if x1 != x2 else None
        k2 = (y4 - y3) / (x4 - x3) if x3 != x4 else None

        # 二者与y轴平行
        if k1 is None and k2 is None:
            if x1 != x3:
                return []
            return [x1, max(min(y1, y2), min(y3, y4))]

        b1 = y1 - k1 * x1 if k1 is not None else None
        b2 = y3 - k2 * x3 if k2 is not None else None

        # 有条线段与y轴平行的情况
        if k1 is None:
            return [x1, k2 * x1 + b2] if is_inside(x3, x4, x1) else []

        if k2 is None:
            return [x3, k1 * x3 + b1] if is_inside(x1, x2, x3) else []

        if k1 == k2:
            # 二者所在直线平行的情况
            if b1 != b2:
                return []
            # 二者所在直线重叠的情况
            return list(max(min(start1, end1), min(start2, end2)))

        # 所在直线相交的情况 求出交点 判断交点是否在两个线段上
        # y = k1 * x + b1 = k2 * x + b2
        # (k1 - k2) * x = b2 - b1
        # x = (b2 - b1) / (k1 - k2)
        rx = (b2 - b1) / (k1 - k2)
        ry = k1 * rx + b1
        if is_inside(x1, x2, rx) and is_inside(x3, x4, rx) and is_inside(y1, y2, ry) and is_inside(y3, y4, ry):
            return [rx, ry]
        return []


if __name__ == '__main__':
    print(Solution().intersection([1, 1],
                                  [-1, 1],
                                  [1, 0],
                                  [-3, 2]))
