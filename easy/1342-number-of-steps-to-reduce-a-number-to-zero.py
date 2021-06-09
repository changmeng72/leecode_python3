class Solution:
    def numberOfSteps(self, num: int) -> int:
        if(num<2):
            return num 
        if(num&0x1==0):
            return self.numberOfSteps(num>>1) + 1
        else:
            return self.numberOfSteps(num-1) +1