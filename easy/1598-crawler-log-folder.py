class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack =['/']
        
        for log in logs:
            if log[0] == '.':
                if log[1] == '.':
                    if(len(stack)>1):
                        stack.pop()
                else:
                    pass
            else:
                stack.append(log)
        return len(stack)-1 if len(stack)>0 else 0