class Solution:
    def __init__(self):
        self.kmp = None

    def KPM(self, needle: str):
        self.kmp = [[0] * 256 for _ in range(len(needle))]

        # 初始化 kmp 第0状态
        for asc in range(256):
            if ord(needle[0]) == asc:
                # 状态推进
                self.kmp[0][asc] = 1

        # 最长重复子前缀 所在状态 aba最长前缀a abab最长前缀ab abac最长前缀无
        X = 0

        for i in range(1, len(needle)):
            for asc in range(256):
                if ord(needle[i]) == asc:
                    # 状态推进
                    self.kmp[i][asc] = i + 1
                else:
                    # 状态回退 到最长重复前缀
                    self.kmp[i][asc] = self.kmp[X][asc]

            # 重复子前缀状态处理
            # aba -> abab 重复子前缀变化 a -> ab
            # aba -> abac 重复子前缀变化 a -> 无
            X = self.kmp[X][ord(needle[i])]

    def kmpStr(self, haystack: str, needle: str) -> int:
        lenTxt = len(haystack)
        lenPat = len(needle)
        self.KPM(needle)

        stateIdx = 0
        for i in range(lenTxt):
            stateIdx = self.kmp[stateIdx][ord(haystack[i])]
            if stateIdx == lenPat:
                return i - lenPat + 1

        return -1

    def KMPOptimize(self, needle: str):
        tmpDic = {k: 0 for k in needle}
        self.kmp = [tmpDic.copy() for _ in range(len(needle))]
        # 初始化 0 状态
        self.kmp[0][needle[0]] = 1

        X = 0
        for i in range(1, len(needle)):
            for k in self.kmp[i]:
                if k == needle[i]:
                    self.kmp[i][k] = i+1
                else:
                    self.kmp[i][k] = self.kmp[X][k]
            X = self.kmp[X][needle[i]]

    def kmpStrOptimize(self, haystack: str, needle: str) -> int:
        lenTxt = len(haystack)
        lenPat = len(needle)
        self.KMPOptimize(needle)

        stateIdx = 0
        for i in range(lenTxt):
            stateIdx = self.kmp[stateIdx].get(haystack[i], 0)
            if stateIdx == lenPat:
                return i - lenPat + 1

        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        lenTxt = len(haystack)
        lenPat = len(needle)
        if lenPat == 0:
            return 0
        if lenTxt < lenPat:
            return -1
        return self.kmpStr(haystack, needle)

    def sunday(self, txt: str, pat: str) -> int:
        def calShiftMap():
            dic = {}
            for i in range(len(pat) - 1, -1, -1):
                if not dic.get(pat[i]):
                    dic[pat[i]] = len(pat) - i
            return dic

        shiftDict = calShiftMap()
        idx = 0

        while idx + len(pat) <= len(txt):
            curStr = txt[idx:idx + len(pat)]

            if curStr == pat:
                return idx
            else:
                if idx + len(pat) == len(txt):
                    return -1
                nextChar = txt[idx + len(pat)]
                shift = shiftDict.get(nextChar, len(pat))
                idx += shift

        return -1


if __name__ == '__main__':
    obj = Solution()
    print(obj.strStr('hello', 'll'))
    print(obj.kmpStrOptimize('aabaacd', 'aac'))
