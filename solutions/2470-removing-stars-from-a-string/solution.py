class Solution:
    def removeStars(self, s: str) -> str:
        result = [''] * len(s)
        w = 0
        
        for r in range(len(s)):
            if s[r] == '*':
                w -= 1  
            else:
                result[w] = s[r]  
                w+= 1
        return "".join(result[:w])

