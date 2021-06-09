class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        newList = []
        
        r = 0
        for word in words:
            odd,even = [],[]
            print(word)
            for i in range(len(word)):
                if i&1:
                    odd.append(word[i])
                else:
                    even.append(word[i])
            odd.sort()
            even.sort()
            newList.append(''.join(odd)+''.join(even))
        c = Counter(newList)
        return len(c.items())