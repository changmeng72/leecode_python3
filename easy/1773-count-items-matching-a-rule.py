class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        key = 0 if ruleKey == 'type' else 1 if ruleKey == 'color' else 2
        r = 0
        for item in items:
            if item[key]==ruleValue:
                r = r+1 
        return r
        
"""
 def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        
        idx_k = 0 if ruleKey == 'type' else (1 if ruleKey == 'color' else 2)
        return sum(x[idx_k] == ruleValue for x in items)
"""