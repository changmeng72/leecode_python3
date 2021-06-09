class Solution:
    def findComplement(self, num: int) -> int:
        return (1<<(floor(math.log(num,2))+1)) - 1 -num
        
        """
        left,right = 31,1
        
        if num> (1<<31) :
            return ~num
        if num==0 or num==1:
            return 1-num
        while left>right+1:
            mid = (left+right+1)//2
            t = 1<<mid
            if num > t:
                right = mid
            elif num< t:
                left = mid
            else:
                return t-1
        return (1<<left)-1-num
 """
                
        