class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(subs[::-1] for subs in s.split(' '))