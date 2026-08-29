class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # initialise hash map for row, col, squares
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        # loop through board
        for r in range(9):
            for c in range(9):
                # skip if "."
                if board[r][c] == ".":
                    continue

                # check for duplicates in each list
                if (board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    # return false
                    return False

                # update value accordingly
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        # return true
        return True