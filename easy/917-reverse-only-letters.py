class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        def isChar(c):
            return  True  if ord('z')>=ord(c)>=ord('a') or ord('Z')>=ord(c)>=ord('A') else False
        
        right = len(s)-1
        left = 0
        charArray = [c for c in s]        
        
        while left<right:
            print(charArray,right)
            while right>-1 and isChar(charArray[right])==False:
                right -= 1
            if(not right>left):
                break
            while isChar(charArray[left])==False:
                left += 1
            if(right>-1 and left < right):
                charArray[left],charArray[right] =  charArray[right],charArray[left]
                left  += 1
                right -= 1
                
        return ''.join(charArray)
            
        