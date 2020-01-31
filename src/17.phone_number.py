class Solution:
    def __init__(self):
        self.result = []
        self.digitMap = {
                "2":"abc",
                "3":"def",
                "4":"ghi",
                "5":"jkl",
                "6":"mno",
                "7":"pqrs",
                "8":"tuv",
                "9":"wxyz"
            }
        self.tmpStrList = []

    def letterCombinations(self, digits: str):
        if digits:
            self.recursive(digits, 0)
        return self.result

    def recursive(self, digits, i):
        if i >= len(digits):
            self.result.append(''.join(self.tmpStrList))
        else:
            theStr = self.digitMap.get(digits[i])
            for char in theStr:
                self.tmpStrList.append(char)
                self.recursive(digits, i+1)
                self.tmpStrList.pop()


if __name__ == '__main__':
    s = Solution()
    s.letterCombinations("23")
    print(s.result)
