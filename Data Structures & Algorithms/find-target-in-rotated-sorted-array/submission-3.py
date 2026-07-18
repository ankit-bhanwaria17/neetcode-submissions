class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        mid = left
        print(f"Mid ----> {mid}")
        left, right = 0, len(nums)-1
        if nums[mid] <= target <= nums[right]:
            left = mid
        elif mid != 0 and (nums[left] <= target <= nums[mid-1]):
            right = mid - 1
        else:
            return -1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return -1