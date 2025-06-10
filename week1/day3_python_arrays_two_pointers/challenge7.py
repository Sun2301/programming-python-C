# Challenge 7: Valid Palindrome (LeetCode)
# Source: https://leetcode.com/problems/valid-palindrome/
# Goal: Check if a string is a palindrome, ignoring non-alphanumeric characters and case


class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = "".join([c for c in s.lower() if c.isalnum()])

        p1,p2 = 0,len(p)-1

        while p1<p2 :
            if p[p1] != p[p2] :
                return False
            p1 += 1
            p2 -= 1
            
        return True

# Example usage
check = Solution()
s = input("Enter a string: ")
result = check.isPalindrome(s)
print(f"Is '{s}' a palindrome? {result}")