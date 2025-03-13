"""
Bitonic Point - Find the Maximum Element

Given an array of integers `arr[]` that is first strictly increasing 
and then maybe strictly decreasing, find the bitonic point (maximum element).
A Bitonic Point is a point before which elements are strictly increasing 
and after which elements are strictly decreasing.

### Examples:
Input: arr[] = [1, 2, 4, 5, 7, 8, 3]
Output: 8
Explanation: Elements before 8 are strictly increasing [1, 2, 4, 5, 7] 
and elements after 8 are strictly decreasing [3].

Constraints:
1 <= arr.length <= 1000
-10^6 <= arr[i] <= 10^6
"""

from typing import List

class Solution:
    def findMaximum(self, arr: List[int]) -> int:
        """
        Finds the bitonic point (maximum element) in the given array.
        Time Complexity: O(log n)
        """
        n = len(arr)
        start, end = 0, n - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            # Check if mid is the peak element
            if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == n - 1 or arr[mid] > arr[mid + 1]):
                return arr[mid]
            
            # If left neighbor is greater, move left
            if mid > 0 and arr[mid - 1] > arr[mid]:
                end = mid - 1
            else:  # Else move right
                start = mid + 1
        
        return -1  # This case should never occur

# Example Usage:
# sol = Solution()
# print(sol.findMaximum([1, 2, 4, 5, 7, 8, 3]))  # Output: 8
