class RecentCounter:

    def __init__(self):
        self.buffer=[]
        

    def ping(self, t: int) -> int:
        while len(self.buffer)>0 and t-self.buffer[0] > 3000:
            self.buffer.pop(0) 
        self.buffer.append(t)
        return len(self.buffer)