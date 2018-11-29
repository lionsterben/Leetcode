class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        class Trie:
            def __init__(self):
                self.word = None
                self.children = [None for _ in range(26)]
        root = Trie()
        for word in words:
            st = root
            for char in word:
                # print(st.val)
                # if st.children[ord(word[idx])-ord('a')] == None:
                #     cc = trie(word[idx])
                #     if idx == len(word)-1:
                #         cc.isword = 1
                #     st.children[ord(word[idx])-ord('a')] = cc
                # st = st.children[ord(word[idx])-ord('a')]
                idx = ord(char) - ord('a')
                if st.children[idx] == None:
                    st.children[idx] = Trie()
                st = st.children[idx]
            st.word = word                 
        
        row, col, res = len(board), len(board[0]), []
        def isValid(i, j):
            return i>=0 and i<row and j>=0 and j<col
        
        def dfs(i, j, node):
            if not isValid(i, j):
                return
            char = board[i][j]
            if char == '*' or node.children[ord(char)-ord('a')] == None:
                return
            node = node.children[ord(char)-ord('a')]
            if node.word != None:
                res.append(node.word)
                node.word = None
            board[i][j] = '*'
            dfs(i-1, j, node)
            dfs(i+1, j, node)
            dfs(i, j-1, node)
            dfs(i, j+1, node)
            board[i][j] = char
        for i in range(row):
            for j in range(col):
                    dfs(i, j, root)
        return res

# trie树的children对应board现有的值，word最后一个字符对应的trie节点存储word，关键是对应关系