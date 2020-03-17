from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        len_word = len(words[0])
        len_all = len_word * len(words)
        words = Counter(words)

        result = []

        for i in range(len(s) - len_all + 1):
            start = i
            word_dict = {}
            # 滑动窗口，比较len_word个字符
            while start <= i + len_all - len_word:
                cur_word = s[start:start+len_word]
                # 如果当前单词不在words 或者 单词累计次数大于words中的单词次数 则进入下一个窗口比较
                if cur_word not in words or word_dict.get(cur_word, 0) >= words[cur_word]:
                    break
                word_dict[cur_word] = word_dict.get(cur_word, 0) + 1
                start += len_word
            else:
                result.append(i)

        return result


if __name__ == '__main__':
    assert Solution().findSubstring('ababaab', ["ab", "ba", "ba"]) == [1]
