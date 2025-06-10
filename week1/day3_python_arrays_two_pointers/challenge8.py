# Challenge 8: Container With Most Water
# Source: https://leetcode.com/problems/container-with-most-water/
# Goal: Find the maximum area of water that can be contained between two lines

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1, p2 = 0, len(height) - 1
        a = 0

        while p1 < p2:
            h1, h2 = height[p1], height[p2]
            a = max(a, min(h1, h2) * (p2 - p1))

            if h1 < h2:
                p1 += 1
            else:
                p2 -= 1

        return a
    
# Example usage
check = Solution()
height = list(map(int, input("Enter heights separated by spaces: ").split()))
result = check.maxArea(height)
print(f"The maximum area of water that can be contained is: {result}")