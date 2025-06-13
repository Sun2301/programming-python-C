# Challenge 9 : Maximum Average Subarray I (LeetCode)
# Source: https://leetcode.com/problems/maximum-average-subarray-i/
# Goal: Find the maximum average of a contiguous subarray of size k

from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[:k])
        maxtotal = summ
        for j in range(1, len(nums) - k + 1):
            summ += nums[j + k - 1] - nums[j - 1]
            maxtotal = max(maxtotal, summ)
        return maxtotal/k
    
# Example usage
check = Solution()
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
k = int(input("Enter the size of the subarray (k): "))
result = check.findMaxAverage(nums, k)
print(f"The maximum average of a contiguous subarray of size {k} is: {result:.2f}")
# Note: The result is formatted to two decimal places for better readability
