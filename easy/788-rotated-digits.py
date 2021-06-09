class Solution:
    def rotatedDigits(self, n: int) -> int:
        goodnums = set([2,5,6,9])
        badnums = set([3,4,7])
        ans = 0
        for  i in range(1,n+1):
            good = False
            num = i
            while num:
                remains = num % 10
                if remains in goodnums:
                    good = True
                elif remains in badnums:
                    good = False
                    break
                num //= 10
                
            if good:
                ans += 1
        return ans
        