INT_MAX = (1 << 31) - 1
INT_MIN = -1 << 31


class Solution:
    def myAtoi(self, str_: str) -> int:
        if not str_:
            return 0

        idx = 0
        for c in str_:
            if c == ' ':
                idx += 1
            else:
                break

        if idx >= len(str_):
            return 0

        result = 0
        sign = 1

        if str_[idx] == '-':
            sign = -1
            idx += 1
        elif str_[idx] == '+':
            idx += 1

        for i in range(idx, len(str_)):
            if '0' <= str_[i] <= '9':
                result = result * 10 + int(str_[i])
            else:
                break

        result *= sign

        if result > INT_MAX:
            result = INT_MAX
        elif result < INT_MIN:
            result = INT_MIN

        return result
