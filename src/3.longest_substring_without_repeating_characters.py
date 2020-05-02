class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memory = {}
        res = 0
        head = 0
        for i, v in enumerate(s):
            if v in memory:
                head = max(head, memory[v] + 1)
            memory[v] = i
            cur = i - head + 1
            res = res if res >= cur else cur
        return res
