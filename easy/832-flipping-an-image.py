class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for r in image:
            r.reverse()
            for i in range(len(r)):
                r[i]=1 if r[i]==0 else 0
        return image
        
  """      
        return [ [ 1 if r[i]==0 else 0 for i in range(len(r.reverse()))] for r in image]
  """