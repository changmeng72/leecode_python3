class Solution:
    def searchchar(self,w1:str,w2:str)->bool:
        cdict = {}
        for c in w2:
            cdict[c] = cdict.get(c,0) + 1
        for c in w1:
            t = cdict.get(c,0)
            if(t==0):
                return False
            else:
                cdict[c] = t-1
        return True
    
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        processed_plate = []
        t = ord('a') - ord('A')
        for c in licensePlate:
            if ord('a')<=ord(c)<= ord('z'):
                processed_plate.append(c)
            elif ord('A')<=ord(c)<= ord('Z'):
                processed_plate.append(chr(ord(c) + t))
        
        
        words.sort(key=lambda x: len(x))
        
        for word in words:
            if len(processed_plate)>len(word):
                continue
            else:
                if self.searchchar(processed_plate,word):
                    return word
        return None
                