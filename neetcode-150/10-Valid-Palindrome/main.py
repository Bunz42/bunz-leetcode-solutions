class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''.join(c for c in s if c.isalnum()).lower()
        
        p1 = 0
        p2 = len(new_str) - 1

        while p1 < p2:
            if(new_str[p1] != new_str[p2]):
                return False
            p1 += 1
            p2 -= 1
        
        return True
