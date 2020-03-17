class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        if not chars or not words:
            return 0

        len_sum = 0
        chars_dict = {}
        for char in chars:
            chars_dict[char] = chars_dict.get(char, 0) + 1

        for word in words:
            if not word:
                continue
            word_dict = {}
            for char in word:
                word_dict[char] = word_dict.get(char, 0) + 1
                if word_dict[char] > chars_dict.get(char, 0):
                    break
            else:
                len_sum += len(word)

        return len_sum
