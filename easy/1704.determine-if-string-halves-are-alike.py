class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        n = len(s)//2
        for i in range(len(s)//2):
            if s[i] in vowels:
                count += 1
            if s[i+n] in vowels:
                count -=1
        return count==0