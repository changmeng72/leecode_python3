class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9
    
    """
    def addDigits_helper(self, num: int):
        s = 0
        while num > 0:
            s += num % 10
            num //= 10
        return s
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = self.addDigits_helper(num)
        return num
    """        
        