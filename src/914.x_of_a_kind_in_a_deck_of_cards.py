from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = {}
        for digit in deck:
            count[digit] = count.get(digit, 0) + 1
        for i in range(2, min(count.values()) + 1):
            for dc in count.values():
                if dc % i != 0:
                    break
            else:
                return True
        return False
