from typing import List


class Solution:
    def numRookCaptures1(self, board: List[List[str]]) -> int:
        x, y = 0, 0
        for x_ in range(len(board)):
            for y_ in range(len(board[x])):
                if board[x_][y_] == 'R':
                    x, y = x_, y_
                    break
        x_str = ''.join(board[x][:]).replace('.', '')
        y_str = ''.join([row[y] for row in board]).replace('.', '')

        return x_str.count('Rp') + x_str.count('pR') + y_str.count('Rp') + y_str.count('pR')

    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook = 'R'
        blank = '.'
        pawn = 'p'

        x, y = 0, 0
        for x_ in range(len(board)):
            for y_ in range(len(board[x])):
                if board[x_][y_] == rook:
                    x, y = x_, y_
                    break

        capture = 0
        dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

        for i in range(4):
            step = 1
            while True:
                cur_x = x + dx[i] * step
                cur_y = y + dy[i] * step
                step += 1
                if cur_x >= len(board) or cur_x < 0 or cur_y >= len(board[cur_x]) or cur_y < 0:
                    break
                if board[cur_x][cur_y] == blank:
                    continue
                if board[cur_x][cur_y] == pawn:
                    capture += 1
                break

        return capture
