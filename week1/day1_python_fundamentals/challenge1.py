# Challenge 1: Two Sum (LeetCode)
# Source: https://leetcode.com/problems/two-sum/
# Goal: Find indices of two numbers that add up to a target value

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force solution
        # Time complexity: O(n^2)
        """  for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        # If no solution is found, return an empty list
        return []
        """
        # # Optimized solution using a hash map
        # # Time complexity: O(n)
        
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []
check = Solution()  
# Example usage
nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target number: "))
result = check.twoSum(nums, target)
print(f"Indices of the two numbers that add up to {target}: {result}")

        