MAX_INT = (1 << 31) - 1
MIN_INT = -1 << 31


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = False
        if dividend < 0:
            dividend = -dividend
            neg = not neg
        if divisor < 0:
            divisor = -divisor
            neg = not neg

        result = 0

        # 一个数能 减去 多少倍除数 就至少是除数多少倍
        while dividend >= divisor:
            mul_divisor = divisor
            multiple = 1
            while True:
                mul_divisor, mul_divisor1 = mul_divisor << 1, mul_divisor
                if mul_divisor <= dividend:
                    multiple <<= 1
                else:
                    dividend -= mul_divisor1
                    result += multiple
                    break

        if neg:
            result = -result

        return result if not result < MIN_INT and not result > MAX_INT else MAX_INT


if __name__ == '__main__':
    assert Solution().divide(-2147483648, -1) == MAX_INT
