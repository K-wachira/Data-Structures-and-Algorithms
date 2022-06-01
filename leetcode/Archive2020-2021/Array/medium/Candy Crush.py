class Solution(object):
    def candyCrush(self, board):
        R, C = len(board), len(board[0])
        todo = False

        for r in range(R):
            for c in range(C-2):
                if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                    board[r][c] = board[r][c+1] = board[r][c+2] = - \
                        abs(board[r][c])
                    todo = True

        for r in range(R-2):
            for c in range(C):
                if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                    board[r][c] = board[r+1][c] = board[r+2][c] = - \
                        abs(board[r][c])
                    todo = True

        for c in range(C):
            wr = R-1
            for r in range(R-1, -1, -1):
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for wr in range(wr, -1, -1):
                board[wr][c] = 0

        return self.candyCrush(board) if todo else board


# board = [[110, 5, 112, 113, 114], [210, 211, 5, 213, 214], [310, 311, 3, 313, 314], [410, 411, 412, 5, 414], [
#     5, 1, 512, 3, 3], [610, 4, 1, 613, 614], [710, 1, 2, 713, 714], [810, 1, 2, 1, 1], [1, 1, 2, 2, 2], [4, 1, 4, 4, 1014]]
# obj = Solution()
# output = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [110, 0, 0, 0, 114], [210, 0, 0, 0, 214], [310, 0, 0,
#                                                                                                         113, 314], [410, 0, 0, 213, 414], [610, 211, 112, 313, 614], [710, 311, 412, 613, 714], [810, 411, 512, 713, 1014]]
# print(obj.candyCrush(board) == output)



class Solution:
    def candyCrush(self, board):
        board_changed = False
        Rows = len(board)
        Cols = len(board[0])
        cells_to_change = []
        for row in range(Rows):
            if self.slidingWindow(row, 0, board[row], True):
                cells_to_change.extend(
                    self.slidingWindow(row, 0, board[row], True))

        for col in range(Cols):
            temp = []
            for row in range(Rows):
                temp.append(board[row][col])
            if self.slidingWindow(row, col, board[row], True):
               cells_to_change.extend(self.slidingWindow(row, col, temp, False))
        for row, col in cells_to_change:
            board[row][col] = 0
            board_changed = True
        C = Cols
        R = Rows
        for c in range(C):
            wr = R-1
            for r in range(R-1, -1, -1):
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for wr in range(wr, -1, -1):
                board[wr][c] = 0
        return self.candyCrush(board) if board_changed else board

    def slidingWindow(self, row, col, arr, isRows):
        result = []
        window = []
        n = len(arr)
        slow, fast = arr[0], 0

        for i in range(n):
            if arr[i] == 0: continue
            if arr[i] != slow:
                if len(window) > 2:
                    result.extend(window)
                window.clear()
                slow = arr[i]
            if isRows:
                window.append((row, i))
            else:
                window.append((i, col))
        if len(window) > 2:
            result.extend(window)
        return result


# board = [[110, 5, 112, 113, 114], [210, 211, 5, 213, 214], [310, 311, 3, 313, 314], [410, 411, 412, 5, 414], [
#     5, 1, 512, 3, 3], [610, 4, 1, 613, 614], [710, 1, 2, 713, 714], [810, 1, 2, 1, 1], [1, 1, 2, 2, 2], [4, 1, 4, 4, 1014]]
# obj = Solution()
# output = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [110, 0, 0, 0, 114], [210, 0, 0, 0, 214], [310, 0, 0,
#                                                                                                         113, 314], [410, 0, 0, 213, 414], [610, 211, 112, 313, 614], [710, 311, 412, 613, 714], [810, 411, 512, 713, 1014]]
# print(obj.candyCrush(board) == output)




# # def trs(nums):

# #     pos = 0

# #     for i in range(len(nums)):
# #         el = nums[i]
# #         if el == 0:
# #             nums[pos], nums[i] = nums[i], nums[pos]
# #             pos += 1
# #     return nums


# arr = [12, 14, 0, 0, 0, 4, 0, 4]
# print(trs(arr))

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
C = len(arr)
for i in range(C, -4, -2):
    print(i)

sh