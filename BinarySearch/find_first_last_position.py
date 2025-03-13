# Binary Search Algorithm to Find First and Last Position of an Element in a Sorted Array
# Problem Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List

class Solution:
    def firstPosition(self, nums: List[int], startIdx: int, endIdx: int, x: int) -> int:
        """Finds the first occurrence of x using binary search."""
        if endIdx < startIdx:
            return -1
        res = -1
        while startIdx <= endIdx:
            mid = startIdx + (endIdx - startIdx) // 2
            if nums[mid] == x:
                res = mid
                endIdx = mid - 1  # Search in the left half
            elif nums[mid] < x:
                startIdx = mid + 1
            else:
                endIdx = mid - 1
        return res

    def lastPosition(self, nums: List[int], startIdx: int, endIdx: int, x: int) -> int:
        """Finds the last occurrence of x using binary search."""
        if endIdx < startIdx:
            return -1
        res = -1
        while startIdx <= endIdx:
            mid = startIdx + (endIdx - startIdx) // 2
            if nums[mid] == x:
                res = mid
                startIdx = mid + 1  # Search in the right half
            elif nums[mid] < x:
                startIdx = mid + 1
            else:
                endIdx = mid - 1
        return res

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Returns the first and last position of `target` in `nums`.
        If `target` is not found, returns [-1, -1].
        """
        if not nums:
            return [-1, -1]

        firstIdx = self.firstPosition(nums, 0, len(nums) - 1, target)
        lastIdx = self.lastPosition(nums, 0, len(nums) - 1, target)

        return [firstIdx, lastIdx]

# Example:
if __name__ == "__main__":
    solution = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(solution.searchRange(nums, target))  # Output: [3, 4]
