# Search insert position
# Source: https://leetcode.com/problems/search-insert-position/
# Goal: Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while l <= r :
            mid =(l+r)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            elif target > nums[mid] :
                l = mid + 1
        return l
    
# Example usage
check = Solution()
nums = list(map(int, input("Enter the sorted array elements separated by spaces: ").split()))
target = int(input("Enter the target value to search for: "))
result = check.searchInsert(nums, target)
if target in nums:
    print(f"The target value {target} is found at index: {result}")
else:
    print(f"The target value {target} should be inserted at index: {result}")
