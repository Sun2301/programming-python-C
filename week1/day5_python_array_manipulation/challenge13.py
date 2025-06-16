# Challenge 13 : Plus One
# Source: https://leetcode.com/problems/plus-one/
# Goal: Given a non-empty array of digits representing a non-negative integer, increment the integer by one and return the resulting array of digits.


from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        

        for i in range(len(digits)-1,-1,-1) :
            if digits[i] < 9 :
                digits[i] = 0
              
            else :
                digits[i] += 1
                return digits
        return [1] + digits

# Example usage
check = Solution()
digits = list(map(int, input("Enter the digits of the number separated by spaces: ").split()))
result = check.plusOne(digits)
print(f"The resulting array after incrementing the number is: {result}")