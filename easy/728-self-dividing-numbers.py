class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        r = []
        for i in range(left,right+1):
            j = i%10  
            k = i
            while k>0 and j!=0 and i%j==0:
                k = k//10
                j = k%10
                
            if(k==0):
                r.append(i)
        return r