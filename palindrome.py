#Leet code problem 9. Palindrome number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        Reversed = x[::-1]
        if Reversed == x:
            return True
        else:
            return False              
