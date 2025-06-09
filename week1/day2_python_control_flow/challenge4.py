# Challenge 4: Valid Anagram (LeetCode)
# Source: https://leetcode.com/problems/valid-anagram/
# Goal: Determine if two strings are anagrams of each other

from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        d = {}
        for l in s:
            d[l]=d.get(l,0)+1

        for le in t:
            if le not in d or d[le] == 0:
                return False
            d[le] -= 1

        return True

# Example usage
check = Solution()
s = input("Enter first string: ")
t = input("Enter second string: ")
result = check.isAnagram(s, t)
print(f"Are '{s}' and '{t}' anagrams? {result}")