class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen = set()

            for c in range(9):
                value = board[r][c]
                 
                
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)
        for c in range(9):
            seen = set()

            for r in range(9):
                value = board[r][c]
                 
                
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)
        
        for boxRow in range(0, 9, 3):
            

            for boxCol in range(0, 9, 3):
                seen = set()

                for r in range(boxRow, boxRow + 3):
                    for c in range(boxCol, boxCol + 3):
                        value = board[r][c]



                        if value == ".":
                            continue
                        if value in seen:
                            return False
                        seen.add(value)

        return True


