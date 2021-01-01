class Solution:
    def isPalindrome(self, x: int) -> bool:
        r = ''
        for i in str(x):
            r = i + r
        if r == str(x):
            return True
        else:
            return False
