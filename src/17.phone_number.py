class Solution:
    def __init__(self):
        self.digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

    def letterCombinations(self, digits: str):
        result = []

        def recursive(tmp_list=None, idx=0):
            if tmp_list is None:
                tmp_list = []
            if idx >= len(digits):
                result.append(''.join(tmp_list))
            else:
                map_str = self.digit_map.get(digits[idx])
                for char in map_str:
                    tmp_list.append(char)
                    recursive(tmp_list, idx+1)
                    tmp_list.pop()
        recursive()
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))
