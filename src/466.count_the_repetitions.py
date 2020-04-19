class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        """理解了循环节, 思路就清晰了, 精彩"""
        if n1 == 0:
            return 0

        s1_cnt, s2_cnt, index = 0, 0, 0
        recall = dict()

        # 简单来讲每个循环节 就是 m1个s1 包含了 m2个s2 加一个未匹配完的 s2[:index]
        # 例如 循环节是 2 个 s1 包含了 1个s2多一点 也就是 s2 + s2[:index]
        # 但是最后这个未匹配完的s2[:index]在循环节中是抛弃的, 不计入s2_cnt
        # 只有剩下的不构成循环节的部分 继续从s2[index]开始匹配

        # 疑问: 循环节中最后s2[:index] 抛弃没有问题吗? 那如果它不抛弃被接着计算的话 结果会不一样的吧
        # 如果不被抛弃接着计算的话能计算出更多的s2 那循环节肯定就不是这个样子了
        # 循环节中多少个s1 包含多少个 s2 已经是最优值了,
        while True:
            s1_cnt += 1
            for c in s1:
                if s2[index] == c:
                    index += 1
                    if index == len(s2):
                        s2_cnt, index = s2_cnt + 1, 0

            # s1 用完 没有找到循环节, 相当于暴力解决了
            if s1_cnt == n1:
                return s2_cnt // n2

            # 第二次 找到 index 就 相当于找到循环节了
            if index in recall:
                # 1.123434343    1234不是循环节 34才是
                s1_pre, s2_pre = recall[index]
                first_loop = (s1_pre, s2_pre)
                in_loop = (s1_cnt - s1_pre, s2_cnt - s2_pre)
                break
            else:
                recall[index] = (s1_cnt, s2_cnt)

        # n1 个 s1 包含 s2 的个数
        # 1234 出现34的次数 + 3434(循环节) 出现34的次数 + 3(假装是剩余的s1) 出现34的个数
        ans = first_loop[1] + (n1 - first_loop[0]) // in_loop[0] * in_loop[1]
        # 处理剩下的s1
        rest = (n1 - first_loop[0]) % in_loop[0]
        for i in range(rest):
            for c in s1:
                if s2[index] == c:
                    index += 1
                    if index == len(s2):
                        ans, index = ans + 1, 0

        return ans // n2

