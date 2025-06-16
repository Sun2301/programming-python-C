# Challenge 12: Move Zeroes
# Source: https://leetcode.com/problems/move-zeroes/
# Goal: Move all zeroes in the array to the end while maintaining the relative order of non-zero elements

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
       
        j  = 0
        for i in range(len(nums)):
            if nums[i] != 0 :
                nums[j] = nums[i]
                j += 1
        nums[j:] = [0]*(len(nums)-j)
        

# Example usage
check = Solution()
nums = list(map(int, input("Enter the array elements separated by spaces: ").split()))
check.moveZeroes(nums)
print(f"The array after moving zeroes is: {nums}")