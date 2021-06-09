class OrderedStream:

    def __init__(self, n: int):
        self.nextInx = 0
        self.buffer = [None for i in range(n)]     
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey = idKey-1
        self.buffer[idKey] = value
        if idKey==self.nextInx:
            self.nextInx = self.buffer.index(None,idKey)             
            return self.buffer[idKey: self.nextInx] 
        return []
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)


 