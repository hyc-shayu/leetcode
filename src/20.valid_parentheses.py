class Solution:
    def isValid(self, s: str) -> bool:
        """

        :param s: str
        :return: bool
        """
        map_p = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            left = map_p.get(c)
            if left is None:
                stack.append(c)
            elif len(stack) > 0 and stack.pop() == left:
                continue
            else:
                return False
        return len(stack) == 0


if __name__ == '__main__':
    test_input = "()()()"
    obj = Solution()
    print(obj.isValid(test_input))
