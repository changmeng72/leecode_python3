class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        d = {}
        res = []
        for i in range(len(row)):
            for c in row[i]:
                d[c] = i
            for c in row[i].upper():
                d[c] = i
                
        for word in words:
            firstc = d[word[0]]
            match = True
            for i in range(1,len(word)):
                if(d[word[i]]!=firstc):
                    match = False
                    break
            if match == True:
                res.append(word)
        return res