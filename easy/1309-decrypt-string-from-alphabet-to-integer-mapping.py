

class Solution:
    def freqAlphabets(self, s: str) -> str:
        r = []
        l = len(s)
        i = 0
        while i<l:
            if(i+2<l):
                if s[i+2] == '#':
                    r.append(chr(int(s[i:i+2])-10 + ord('j')))
                    i += 3
                else:
                    r.append(chr(int(s[i])-1 + ord('a')))
                    i += 1
            else:
                for j in range(i,l):
                    r.append(chr(int(s[i])-1 + ord('a')))
                    i += 1
        return ''.join(r)
        
"""
mapping = { '1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i',
               '10':'j','11':'k','12':'l','13':'m','14':'n','15':'o','16':'p',
               '17':'q','18':'r','19':'s','20':'t','21':'u','22':'v','23':'w','24':'x',
               '25':'y','26':'z'
              }
    
    # Instead of iterating forward, read the string backward 
	i = len(s) - 1
    ans = ''
    
    while i >=0:
        if s[i] == '#':
            ans = mapping[s[i-2:i]] + ans
            i -= 3
        else:
            ans = mapping[s[i]] + ans
            i -= 1
    
    return ans
"""