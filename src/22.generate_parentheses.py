class Solution:
    def dp(self, n: int):
        """
        leetcode 动态规划 解法
        :type n: int
        """
        if n == 0:
            return []
        total_l = []
        total_l.append([None])  # 0组括号时记为None
        total_l.append(["()"])  # 1组括号只有一种情况
        for i in range(2, n + 1):  # 开始计算i组括号时的括号组合
            tmp_list = []
            for j in range(i):  # 开始遍历 p q ，其中p+q=i-1 , j 作为索引
                now_list1 = total_l[j]  # p = j 时的括号组合情况
                now_list2 = total_l[i - 1 - j]  # q = (i-1) - j 时的括号组合情况
                for k1 in now_list1:
                    for k2 in now_list2:
                        if k1 is None:
                            k1 = ""
                        if k2 is None:
                            k2 = ""
                        el = "(" + k1 + ")" + k2
                        tmp_list.append(el)  # 把所有可能的情况添加到 tmp_list 中
            total_l.append(tmp_list)  # l这个list就是i组括号的所有情况，添加到total_l中，继续求解i=i+1的情况
        return total_l[n]

    def generateParenthesis(self, n: int):
        result = []

        def backtrack(s='', left=0, right=0, max_=n):
            if len(s) == 2 * max_:
                result.append(s)
            if left < max_:
                backtrack(s + '(', left + 1, right, max_)
            if right < left:
                backtrack(s + ')', left, right + 1, max_)

        backtrack()
        return result

    def generateParenthesis1(self, n: int):
        result = []

        def backtrack(tmp_list=None, left=0, right=0):
            if tmp_list is None:
                tmp_list = []
            # 当左括号为0 右括号全部释放
            if left == n:
                result.append(''.join(tmp_list + [')'] * (n - right)))
                return

            # 当左括号小于右括号 并且 左括号大于0 时 选择 左括号或右括号
            if left < n:
                tmp_list.append('(')
                backtrack(tmp_list, left+1, right)
                tmp_list.pop()
            if right < left:
                tmp_list.append(')')
                backtrack(tmp_list, left, right+1)
                tmp_list.pop()

        backtrack()
        return result


if __name__ == '__main__':
    obj = Solution()
    print(obj.generateParenthesis(3))
    print(obj.generateParenthesis1(3))
    assert obj.generateParenthesis(3) == obj.generateParenthesis1(3)
