class Solution:
    def reverseVowels(self, s: str) -> str:
        s_t=list(s)
        l=0
        r=len(s)-1
        vowels = set("aeiouAEIOU")
        while l<r:
            while l<r and s_t[l] not in vowels:
                l+=1
            while l<r and s_t[r] not in vowels:
                r-=1
            if l<r:
                s_t[l],s_t[r]=s_t[r],s_t[l]
                l+=1
                r-=1
        return"".join(s_t)
                
