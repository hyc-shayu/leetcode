class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        memory = set()
        stack = [(0, 0)]
        while stack:
            remain_x, remain_y = stack.pop()
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                return True
            if (remain_x, remain_y) in memory:
                continue
            memory.add((remain_x, remain_y))
            # 装满x桶
            stack.append((x, remain_y))
            # 装满y桶
            stack.append((remain_x, y))
            # 排空x桶
            stack.append((0, remain_y))
            # 排空y桶
            stack.append((remain_x, 0))

            sum_ = remain_x + remain_y
            # x -> y
            y1 = sum_ if sum_ < y else y
            stack.append((sum_ - y1, y1))
            # y -> x
            x1 = sum_ if sum_ < x else x
            stack.append((x1, sum_ - x1))
        return False

    def canMeasureWaterSelf(self, x: int, y: int, z: int) -> bool:
        memory = set()

        def recursion(water1, water2):
            if water1 + water2 == z:
                return True

            if (water1, water2) in memory:
                return False

            memory.add((water1, water2))

            # 装满一个桶
            def full_jug():
                if water1 == x and water2 == y:
                    return False
                if water1 < x and water2 < y:
                    return recursion(x, water2) or recursion(water1, y)
                # 有一个桶已满, 那么2个桶都会装满
                return recursion(x, y)

            # 清空一个桶
            def clear_jug():
                if water1 == water2 == 0:
                    return False
                if water1 > 0 and water2 > 0:
                    return recursion(0, water2) or recursion(water1, 0)
                return recursion(0, 0)

            # 向某个桶倒水
            def pour_water():
                if water1 == water2 == 0:
                    return False
                if water1 == x and water2 == y:
                    return False

                sum_ = water1 + water2
                # y -> x
                if water1 == 0 or water2 == y:
                    w1 = x if sum_ > x else sum_
                    w2 = sum_ - w1
                # x -> y
                else:
                    w2 = y if sum_ > y else sum_
                    w1 = sum_ - w2
                return recursion(w1, w2)

            return full_jug() or clear_jug() or pour_water()

        return recursion(0, 0)


if __name__ == '__main__':
    solution = Solution()
    assert solution.canMeasureWater(3, 5, 4) is True
