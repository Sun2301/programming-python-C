# Challenge 3: Contains Duplicate (LeetCode)
# Source: https://leetcode.com/problems/contains-duplicate/
# Goal: Check if any value appears at least twice in the array

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = set()
        for num in nums :
            if num in d :
                return True
            d.add(num)
        return False
    

# Example usage
check = Solution()
nums = list(map(int, input("Enter numbers separated by space: ").split()))
result = check.containsDuplicate(nums)
print(f"Contains duplicate: {result}")
        