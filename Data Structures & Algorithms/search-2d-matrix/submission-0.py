class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        top, bottom = 0, r-1
        potentialRow = 0

        while top <= bottom:
            mid = top + (bottom - top)//2
            if matrix[mid][0] == target:
                return True
            elif target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][c-1]:
                top = mid + 1
            else:
                potentialRow = mid
                break

        left, right = 0, c-1
        while left <= right:
            mid = left + (right-left)//2
            if matrix[potentialRow][mid] == target:
                return True
            elif matrix[potentialRow][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False