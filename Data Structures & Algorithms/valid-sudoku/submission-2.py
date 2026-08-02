class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap = defaultdict(set) # key: r(rowNumber), c(colNumber), box(number), value: set()
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                row = f"r{r}"
                col = f"c{c}"
                box = f"b{r//3}{c//3}"
                num = board[r][c]
                if (
                    num in hashmap[row] 
                    or num in hashmap[col] 
                    or num in hashmap[box]
                ):
                    return False
                hashmap[row].add(num)
                hashmap[col].add(num)
                hashmap[box].add(num)
        return True