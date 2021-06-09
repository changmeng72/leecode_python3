class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        r = []
        
        for i in range(len(words[0])):
            find = True
            for j in range(1,len(words)):
                index = words[j].find(words[0][i])
                if index==-1:
                    find = False
                    break
                else:
                    words[j] = words[j].replace(words[0][i],'U',1)
            if(find==True):
                r.append(words[0][i])
        return r
            