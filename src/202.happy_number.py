class Solution:
    def isHappy(self, n: int) -> bool:
        memory = set()
        while n != 1:
            if n in memory:
                return False
            memory.add(n)
            rem_sum = 0
            while n:
                remain = n % 10
                n //= 10
                rem_sum += remain**2
            n = rem_sum
        return True
