class Solution(object):
    def isValidSudoku(self, board):
        return self.isValidRow(board) and self.isValidCol(board) and self.isValidNineCell(board)

    def isValidRow(self, board):
        for r in range(9):
            row = [x for x in board[r] if x != '.'] #행 존재하는 숫자 row에 넣기
            if len(set(row)) != len(row):  # 중복 검사
                return False
        return True

    def isValidCol(self, board):
        for c in range(9):
            col = [board[r][c] for r in range(9) if board[r][c] != '.'] 
            if len(set(col)) != len(col):
                return False
        return True

    def isValidNineCell(self, board):
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                cell = []
                for i in range(3):
                    for j in range(3):
                        num = board[r + i][c + j]
                        if num != '.':
                            cell.append(num)
                if len(set(cell)) != len(cell):
                    return False
        return True