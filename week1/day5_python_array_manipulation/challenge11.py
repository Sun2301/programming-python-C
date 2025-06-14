# Challenge 11: Rotate array (Leetcode 189)
# Source: https://leetcode.com/problems/rotate-array/
# Goal: Rotate the array to the right by k steps, where k is non-negative

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        k %= len(nums)  # In case k is larger than the array length
        """ # Reverse method 
        
        # Firt, let's reverse the entire array
        nums.reverse()
        # Then, reverse the first k elements
        nums[:k] = reversed(nums[:k])
        # Finally, reverse the remaining n-k elements
        nums[k:] = reversed(nums[k:])
        """

        """ Slicing method """
        nums[:] = nums[-k:] + nums[:-k]



# Example usage
check = Solution()
nums = list(map(int, input("Enter the array elements separated by spaces: ").split()))
k = int(input("Enter the number of steps to rotate (k): "))
check.rotate(nums, k)
print(f"The rotated array is: {nums}")
