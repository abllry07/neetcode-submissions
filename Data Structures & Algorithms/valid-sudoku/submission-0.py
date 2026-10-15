class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Thinking, create two hash tables, one for row frequency and one for column frequency. Then, we can check to see if each value appears 9 teams exactly in both tables, then it is valid, else invalid and can abort right away.
        cols = collections.defaultdict(set) 
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r / 3, c / 3)


        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False 
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
                
