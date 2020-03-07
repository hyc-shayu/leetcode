class Solution:
    def __init__(self):
        self.kmp = None

    def _kpm(self, needle: str):
        self.kmp = [[0] * 256 for _ in range(len(needle))]

        # 初始化 kmp 第0状态
        for asc in range(256):
            if ord(needle[0]) == asc:
                # 状态推进
                self.kmp[0][asc] = 1

        # 最长重复子前缀 所在状态 aba最长前缀a abab最长前缀ab abac最长前缀无
        x = 0

        for i in range(1, len(needle)):
            for asc in range(256):
                if ord(needle[i]) == asc:
                    # 状态推进
                    self.kmp[i][asc] = i + 1
                else:
                    # 状态回退 到最长重复前缀
                    self.kmp[i][asc] = self.kmp[x][asc]

            # 重复子前缀状态处理
            # aba -> abab 重复子前缀变化 a -> ab
            # aba -> abac 重复子前缀变化 a -> 无
            x = self.kmp[x][ord(needle[i])]

    def kmp_str(self, haystack: str, needle: str) -> int:
        len_txt = len(haystack)
        len_pat = len(needle)
        self._kpm(needle)

        state_idx = 0
        for i in range(len_txt):
            state_idx = self.kmp[state_idx][ord(haystack[i])]
            if state_idx == len_pat:
                return i - len_pat + 1

        return -1

    def _kmp_optimize(self, needle: str):
        tmp_dic = {k: 0 for k in needle}
        self.kmp = [tmp_dic.copy() for _ in range(len(needle))]
        # 初始化 0 状态
        self.kmp[0][needle[0]] = 1

        x = 0
        for i in range(1, len(needle)):
            for k in self.kmp[i]:
                if k == needle[i]:
                    self.kmp[i][k] = i+1
                else:
                    self.kmp[i][k] = self.kmp[x][k]
            x = self.kmp[x][needle[i]]

    def kmp_str_optimize(self, haystack: str, needle: str) -> int:
        len_txt = len(haystack)
        len_pat = len(needle)
        self._kmp_optimize(needle)

        state_idx = 0
        for i in range(len_txt):
            state_idx = self.kmp[state_idx].get(haystack[i], 0)
            if state_idx == len_pat:
                return i - len_pat + 1

        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        len_txt = len(haystack)
        len_pat = len(needle)
        if len_pat == 0:
            return 0
        if len_txt < len_pat:
            return -1
        return self.kmp_str(haystack, needle)

    def sunday(self, txt: str, pat: str) -> int:
        def cal_shift_map():
            dic = {}
            for i in range(len(pat) - 1, -1, -1):
                if not dic.get(pat[i]):
                    dic[pat[i]] = len(pat) - i
            return dic

        shift_dict = cal_shift_map()
        idx = 0

        while idx + len(pat) <= len(txt):
            cur_str = txt[idx:idx + len(pat)]

            if cur_str == pat:
                return idx
            else:
                if idx + len(pat) == len(txt):
                    return -1
                next_char = txt[idx + len(pat)]
                shift = shift_dict.get(next_char, len(pat))
                idx += shift

        return -1


if __name__ == '__main__':
    obj = Solution()
    print(obj.strStr('hello', 'll'))
    print(obj.kmp_str_optimize('aabaacd', 'aac'))
