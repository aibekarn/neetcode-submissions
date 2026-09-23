class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        d = {')':'(', ']':'[', '}':'{'}

        for ch in s:
            if ch in d.values():
                l.append(ch)
            else: 
                if len(l) == 0:
                    return False
                elif d[ch] != l[-1]:
                    return False
                l.pop()
                
        return len(l) == 0
