class Solution:
    def hasDuplicate(self, nums: List[str]):
        count = []
        for n in nums:
            if n == ".":
                continue
            if n in count:
                return True
            count.append(n)
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Test Row
        for row in board:
            if self.hasDuplicate(row):
                return False
        
        # Test column
        for i in range(9):
            col = []
            for row in board:
                col.append(row[i])
            if self.hasDuplicate(col):
                return False
        
        # Test box
        boxMap = defaultdict(list)
        for i in range(9):
            for j in range(9):
                key = str(i//3) + str(j//3)
                boxMap[key].append(board[i][j])

        for key, value in boxMap.items():
            if self.hasDuplicate(value):
                return False

        return True
