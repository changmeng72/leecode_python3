class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        cur  = s[0]
        cur_count = 0
        max_1_count = 0
        max_0_count = 0
        
        for c in s:
            if c==cur:
                cur_count += 1
            else:
                if c=='1' and cur_count >  max_0_count:
                    max_0_count = cur_count
                elif c=='0' and cur_count >  max_1_count:    
                    max_1_count = cur_count
                cur = c
                cur_count = 1
          
        if c=='1' and cur_count >  max_1_count:
            max_1_count = cur_count
        elif c=='0' and cur_count >  max_0_count:    
            max_0_count = cur_count
        
        return True if max_1_count>max_0_count else False