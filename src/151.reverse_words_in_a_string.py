class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ''

        s = s.strip()
        left, right = 0, 0
        words = []
        for i, c in enumerate(s):
            if c == ' ':
                if left < right:
                    words.append(s[left:right])
                left = i + 1
            else:
                right = i + 1
        words.append(s[left:right])
        return ' '.join(words[::-1])


if __name__ == '__main__':
    sol = Solution()
    assert sol.reverseWords("  hello world!  ") == "world! hello"
