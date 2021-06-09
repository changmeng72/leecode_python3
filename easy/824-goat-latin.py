class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        words = sentence.split(' ')
        for i in range(len(words)):
            if words[i][0] in vowel:
                words[i] = words[i]+'maa'+'a'*i
            else:
                words[i] = words[i][1:] +words[i][0]+'maa'+'a'*i
        return ' '.join(words)