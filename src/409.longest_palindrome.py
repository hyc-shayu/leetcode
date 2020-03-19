class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_dict = {}
        count = 0
        for char in s:
            char_dict[char] = char_dict.get(char, 0) + 1
            if char_dict[char] == 2:
                count += 2
                char_dict.pop(char)
        return count + 1 if char_dict else count
