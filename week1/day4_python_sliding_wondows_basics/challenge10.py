#  Challenge 10: Maximum number of Vowels in a Substring of Given Length (LeetCode)
# Source: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# Goal: Find the maximum number of vowels in any substring of length k

from typing import List

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        max_count = count = sum(1 for ch in s[:k] if ch in vowels)
        for i in range(k, len(s)):
            if s[i] in vowels: 
                count += 1 
            if s[i - k] in vowels: 
                count -= 1 
            max_count = max(max_count, count)

        return max_count
        return vn
    
# Example usage
check = Solution()
s = input("Enter a string: ")
k = int(input("Enter the size of the substring (k): "))
result = check.maxVowels(s, k)
print(f"The maximum number of vowels in a substring of length {k} is: {result}")
