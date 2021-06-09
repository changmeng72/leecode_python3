class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d =  [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        r = set()
        
        for word in words:
            s =''
            for c in word:
                s += d[ord(c)-97]
            r.add(s)
        return len(r)