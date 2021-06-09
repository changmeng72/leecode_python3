class Node:
    def __init__(self,val):
        self.next = None 
        self.val = val


class MyHashSet:
    
    

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket = [None] * 10000
        

    def add(self, key: int) -> None:
        key_t = key % 10000
        if self.bucket[key_t] == None:
            self.bucket[key_t] = Node(key)
        else:
            node = self.bucket[key_t]
            
            while node.val!=key and node.next!=None:
                node = node.next
            if node.val==key:
                return
            else:
                node.next= Node(key) 
        

    def remove(self, key: int) -> None:
        key2 = key % len(self.bucket)
        node = self.bucket[key2] 
        if node == None:
                return 
        if node.val==key:
            self.bucket[key2] = node.next
            return
        prev = node
        node = node.next
        if not node:
            return
        while node and node.val!=key and node.next:
                prev = node
                node = node.next
        if node.val== key:
                prev.next = node.next
        return

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        key2 = key % len(self.bucket)
        if self.bucket[key2]:
            if self.bucket[key2].val==key:
                return True
            else:
                node =  self.bucket[key2]
                node = node.next
                while node:
                    if node.val==key:
                        return True
                    node = node.next
        return False
                
         
