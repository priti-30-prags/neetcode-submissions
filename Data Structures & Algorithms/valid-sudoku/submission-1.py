class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])
        for i in range(row):
            l = []
            for j in range(col):
                if board[i][j] != ".":
                    l.append(board[i][j])
            if len(l)!=len(set(l)):
                return False
        for i in range(row):
            l = []
            for j in range(col):
                if board[j][i] != ".":
                    l.append(board[j][i])
            if len(l)!=len(set(l)):
                return False
        for a in range(0,row,3):
            for b in range(0,col,3):
                l = []
                for i in range(3):
                    for j in range(3):
                        if board[a+i][b+j]!= ".":
                            l.append(board[a+i][b+j])
                if len(l)!=len(set(l)):
                    return False
        return True