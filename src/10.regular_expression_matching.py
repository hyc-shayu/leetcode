class Solution:
    def isMatch(self, s, p):
        if p and s:
            p_last_part = p.split('*')[-1]
            p_last_part = p_last_part.split('.')[-1]
            if not s[::-1].startswith(p_last_part[::-1]):
                return False
        return self.is_match_sub(s, p)

    def is_match_sub(self, s, p):
        if s == '':
            if p == '':
                return True
            # s='' p='a*b*c*.*'
            if len(p) > 1 and p[0] != '*' and p[1] == '*':
                return self.is_match_sub(s, p[2:])
            return False
        if p == '':
            return False
        if p[0] == '*':
            return False
        if s[0] == p[0] or p[0] == '.':
            if len(p) > 1 and p[1] == '*':
                # s="ba" p=".*a*a"
                #       匹配                        不匹配
                return self.is_match_sub(s[1:], p) or self.is_match_sub(s, p[2:])
            return self.is_match_sub(s[1:], p[1:])
        elif len(p) > 1 and p[1] == '*':
            return self.is_match_sub(s, p[2:])
        return False

    def dp_solution(self, text, pattern):
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in (text[i], '.')
                    if j + 1 < len(pattern) and pattern[j + 1] == '*':
                        # +1匹配                            不匹配 丢弃
                        ans = first_match and dp(i + 1, j) or dp(i, j + 2)
                    else:
                        ans = first_match and dp(i + 1, j + 1)
                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)


if __name__ == '__main__':
    solution = Solution()
    str_ = 'ab'
    pattern1 = 'a*b*c*.*'
    assert solution.isMatch(str_, pattern1) is True
    assert solution.dp_solution(str_, pattern1) is True
    str_ = 'ab'
    pattern1 = 'a*c.*'
    assert solution.isMatch(str_, pattern1) is False
    assert solution.dp_solution(str_, pattern1) is False
