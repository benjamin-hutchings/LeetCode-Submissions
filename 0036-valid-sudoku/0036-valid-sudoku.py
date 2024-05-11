import collections

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # Key = (r//3, c//3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                # Check if the value is already present in the current row, column, or square
                if (val in rows[r] or
                    val in cols[c] or
                    val in squares[(r//3, c//3)]):
                    return False
                # Add the value to the respective row, column, and square
                cols[c].add(val)
                rows[r].add(val)
                squares[(r//3, c//3)].add(val)
        return True
