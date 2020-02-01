class Solution:
    def __init__(self):
        self.l = "("
        self.r = ")"
        self.tmp = []
        self.result = []
        self.left = 0
        self.right = 0

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
            l = []
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
                        l.append(el)  # 把所有可能的情况添加到 l 中
            total_l.append(l)  # l这个list就是i组括号的所有情况，添加到total_l中，继续求解i=i+1的情况
        return total_l[n]

    def generateParenthesis(self, n: int):
        result = []

        def backtrack(S='', left=0, right=0, Max=n):
            if len(S) == 2 * Max:
                result.append(S)
            if left < Max:
                backtrack(S + '(', left + 1, right, Max)
            if right < left:
                backtrack(S + ')', left, right + 1, Max)

        # self.generateParenthesis1(n)
        # return self.result
        backtrack()
        return result

    def generateParenthesis1(self, n: int):
        # 当左括号为0 右括号全部释放
        if self.left == n:
            self.result.append(''.join((self.tmp + [self.r] * (n - self.right))))
            return
        # 当左括号小于右括号 并且 左括号大于0 时 选择 左括号或右括号

        # 当左括号等于右括号 只能选择左括号

        # 选择左括号
        self.tmp.append(self.l)
        self.left += 1
        self.generateParenthesis(n)
        self.tmp.pop()
        self.left -= 1

        # 选择右括号
        if self.right < self.left:
            self.tmp.append(self.r)
            self.right += 1
            self.generateParenthesis(n)
            self.tmp.pop()
            self.right -= 1


if __name__ == '__main__':
    obj = Solution()
    print(obj.generateParenthesis(3))
