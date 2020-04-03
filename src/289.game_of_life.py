class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        neighbor = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

        len_x = len(board)
        len_y = len(board[0])

        # 计算周围活细胞数量
        def count_around(x, y):
            alive = 0
            for acc_x, acc_y in neighbor:
                if 0 <= x+acc_x < len_x and 0 <= y + acc_y < len_y and board[x + acc_x][y + acc_y] >= 1:
                    alive += 1
            return alive

        def change(x, y):
            alive = count_around(x, y)
            if board[x][y] == 1:
                if alive < 2 or alive > 3:
                    # 2过去活着 现在死了
                    board[x][y] = 2
            else:
                if alive == 3:
                    # -1过去死了 现在活了
                    board[x][y] = -1

        for x_ in range(len_x):
            for y_ in range(len_y):
                change(x_, y_)

        for x_ in range(len_x):
            for y_ in range(len_y):
                if board[x_][y_] == -1:
                    board[x_][y_] = 1
                if board[x_][y_] == 2:
                    board[x_][y_] = 0
