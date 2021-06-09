class Node:
    def __init__(self,key,val):
        self.next = None
        self.key = key
        self.val = val

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        
        """
        self.buffer = [None for i in range(10000)]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        key_t = key%10000
        if not self.buffer[key_t]:
            self.buffer[key_t] = Node(key,value)
        else:
            n = self.buffer[key_t]
            while n.next and n.key!=key:
                n = n.next
            if n.key!=key:
                n.next = Node(key,value)
            else:
                n.val = value
        return None
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        key_t =  key%10000        
        n = self.buffer[key_t]
        while n:
            if key==n.key:
                return n.val
            n = n.next
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        key_t =  key%10000          
        n = self.buffer[key_t]
        if not n:
            return None
        if n and n.key==key:
            self.buffer[key_t] = n.next
            return None
        prev = self.buffer[key_t]
        n = n.next    
        while n:
            if key==n.key:
                prev.next = n.next
                return
            else:
                prev = n
                n = n.next
        return None
        
