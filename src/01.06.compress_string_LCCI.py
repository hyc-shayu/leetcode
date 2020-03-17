class Solution:
    def compressString(self, str_: str) -> str:
        if not str_:
            return str_

        str_list = [str_[0], 1]
        for char in str_[1:]:
            if char == str_list[-2]:
                str_list[-1] += 1
            else:
                str_list[-1] = str(str_list[-1])
                str_list.append(char)
                str_list.append(1)

        str_list[-1] = str(str_list[-1])

        return str_ if len(str_list) >= len(str_) else ''.join(str_list)
