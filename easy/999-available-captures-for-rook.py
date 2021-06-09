class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        d = [0] * 8
        res = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'p'or board[i][j] == 'B':
                    d[j] = board[i][j]
                if board[i][j] == 'R':
                    for k in range(j-1,-1,-1):
                        if board[i][k] == 'p':
                            res += 1
                            break
                        elif board[i][k] =='B':
                            break
                    for k in range(j+1,8):
                        if board[i][k] == 'p':
                            res += 1
                            break
                        elif board[i][k] =='B':
                            break
                    if d[j]=='p':
                        res += 1;
                    for k in range(i+1,8):
                        if board[k][j] == 'p':
                            res += 1
                            break
                        elif board[k][j] =='B':
                            break
                    return res
        return res   
                    
                        