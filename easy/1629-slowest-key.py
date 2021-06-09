class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        skey , stime = keysPressed[0],releaseTimes[0]
        
        for i in range(1,len(releaseTimes)):
            delta = releaseTimes[i] - releaseTimes[i-1]
            if delta > stime or (delta==stime and ord(skey) < ord(keysPressed[i])):
                skey = keysPressed[i]
                stime = delta
        return skey