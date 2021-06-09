class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        fn = []
        ind = -1
        for k in words:
            index = -1
            ind+=1
            for j in words:
                index+=1
                if k in j and ind != index :
                    fn.append(k)
        res = []
        for s in fn:
            if s not in res:
                res.append(s)
        return res
    """
        res = []
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if(len(words[j])>=len(words[i])):
                    if words[i] in  words[j]:
                        res.append(words[i])
                        
                else:
                    if words[j] in words[i]:
                        res.append(words[j])
                        
                    
        return list(set(res))
    """            
           