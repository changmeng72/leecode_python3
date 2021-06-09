class Solution:
    def interpret(self, command: str) -> str:
        import re
        command = re.sub("\(\)","o",command)
        return re.sub("\(al\)","al",command)