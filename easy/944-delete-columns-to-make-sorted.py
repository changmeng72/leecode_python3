class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        r = 0
        for i in range(len(strs[0])):
            for n in range(1,len(strs)):
                if(strs[n][i]<strs[n-1][i]):
                    r += 1
                    break
        return r

"""
def minDeletionSize(self, strs: List[str]) -> int:
        
        output = 0 
        for s in zip( *strs ):
            if sorted( s ) != list( s ):
                output+=1
                
        return output 
"""