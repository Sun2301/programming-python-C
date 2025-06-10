# Challenge 6: Two Sum II - Input Array Is Sorted (LeetCode)
# Source: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Goal: Find indices of two numbers such that they add up to a specific target

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        p1,p2 = 0,len(numbers)-1
        while p1 < p2 :
            summ = numbers[p1] + numbers[p2]
            if summ == target :
                return [p1 +1, p2 +1]
            elif summ < target :
                p1 += 1
            else :
                p2 -= 1
        return []

# Example usage
check = Solution()
numbers = list(map(int, input("Enter sorted numbers(in non-discreasing order) separated by space: ").split()))
target = int(input("Enter target sum: "))
result = check.twoSum(numbers, target)
print(f"Indices of numbers that add up to {target}: {result}")