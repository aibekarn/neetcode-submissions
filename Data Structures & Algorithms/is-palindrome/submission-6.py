class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) > 1000 or len(s) == 0:
            return s.isascii() 

        cleaned_s = "".join(c for c in s.lower()  if c.isalnum())

        for i in range(len(cleaned_s)//2):
            if cleaned_s[i] == cleaned_s[len(cleaned_s) - 1 - i]:
                continue
            else:
                return False

        return True



    