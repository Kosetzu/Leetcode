# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

class Solution:
    def word_present(self, board, i, j, numrow, numcol, word, incoming_dir, visited):
        if board[i][j] != word[0]:
            return False

        visited[i][j] = True
        
        if len(word) == 1 and board[i][j] == word[0]:
            return True

        # Check the Word DIRECTION -> UP
        if 0 <= (i-1) < numrow and not visited[i-1][j] and incoming_dir != 'U':
            if self.word_present(board, i-1, j, numrow, numcol, word[1:], 'D', visited):
                return True

        # Check the Word DIRECTION -> DOWN
        if 0 <= (i+1) < numrow and not visited[i+1][j] and incoming_dir != 'D':
            if self.word_present(board, i+1, j, numrow, numcol, word[1:], 'U', visited):
                return True

        # Check the Word DIRECTION -> LEFT
        if 0 <= (j-1) < numcol and not visited[i][j-1] and incoming_dir != 'L':
            if self.word_present(board, i, j-1, numrow, numcol, word[1:], 'R', visited):
                return True

        # Check the Word DIRECTION -> RIGHT
        if 0 <= (j+1) < numcol and not visited[i][j+1] and incoming_dir != 'R':
            if self.word_present(board, i, j+1, numrow, numcol, word[1:], 'L', visited):
                return True

        visited[i][j] = False
        return False
    
    def exist(self, board, word):
        m = len(board) #ROW
        n = len(board[0]) #COLUMN

        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.word_present(board,i,j,m,n,word,None, visited):
                    return True
        return False
                    