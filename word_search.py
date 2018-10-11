class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        col = len(board[0])
        # marked = [[-1 for _ in range(col)] for __ in range(row)]
        def isValid(i, j):
            return i>=0 and i<row and j>=0 and j<col
        
        def dfs(i, j, word):
            # print(i,j,word)
            # if i == 0  and j == 1:
            #     print("haha")
            #     print(isValid(i, j))
            #     print(marked[i][j])
            #     print(word)
            marked[i][j] = 0
            if word == "":
                return True
            if board[i][j] == word:
                return True 
            if board[i][j] != word[0]:
                return False
            if isValid(i+1, j) and marked[i+1][j] == -1 and board[i][j] == word[0]:
                # print(i,j,word)
                a1 = dfs(i+1, j, word[1:])
                if a1:
                    return True
                marked[i+1][j] = -1
            if isValid(i, j+1) and marked[i][j+1] == -1 and board[i][j] == word[0]:
                # print(i,j,word)
                a2 = dfs(i, j+1, word[1:])
                if a2:
                    return True
                marked[i][j+1] = -1
            if isValid(i-1, j) and marked[i-1][j] == -1 and board[i][j] == word[0]:
                # print(word)
                a3 = dfs(i-1, j, word[1:])
                if a3:
                    return True
                marked[i-1][j] = -1
            if isValid(i, j-1) and marked[i][j-1] == -1 and board[i][j] == word[0]:
                # print(word)
                a4 = dfs(i, j-1, word[1:])
                if a4:
                    return True
                marked[i][j-1] = -1
            return False
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    marked = [[-1 for _ in range(col)] for __ in range(row)]
                    if dfs(i, j, word):
                        return True
        return False

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        col = len(board[0])
        # marked = [[-1 for _ in range(col)] for __ in range(row)]
        def isValid(i, j):
            return i>=0 and i<row and j>=0 and j<col
        
        def dfs(i, j, word):
            # print(i,j,word)
            # if i == 0  and j == 1:
            #     print("haha")
            #     print(isValid(i, j))
            #     print(marked[i][j])
            #     print(word)
            if len(word) == 0:
                return True
            if not isValid(i,j) or board[i][j] != word[0]:
                return False
            tmp = board[i][j]
            board[i][j] = '*'
            res = dfs(i-1, j, word[1:]) or dfs(i, j-1, word[1:]) or dfs(i+1, j, word[1:]) or dfs(i, j+1, word[1:])
            board[i][j] = tmp
            return res
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    # marked = [[-1 for _ in range(col)] for __ in range(row)]
                    if dfs(i, j, word):
                        return True
        return False