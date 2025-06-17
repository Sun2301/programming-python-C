
# Challenge 14: Binary Search(LeetCode 704)
# Source: https://leetcode.com/problems/binary-search/
# Goal: Implement binary search to find the index of a target value in a sorted array.


from typing import List

def find(nums : List[int],  target : int) -> int :


        l,r = 0, len(nums)-1
        while l <= r :
            mid = int((l+r)/2)
            if target == nums[mid] :
                return mid
            elif target < nums[mid] :
                r = mid - 1
            elif target > nums[mid] :
                l = mid + 1

        return -1

# Example usage
nums = list(map(int, input("Enter the sorted array elements separated by spaces: ").split()))
target = int(input("Enter the target value to search for: "))
result = find(nums, target)
if result != -1:
    print(f"The target value {target} is found at index: {result}")
else:
    print(f"The target value {target} is not found in the array.")
    
    