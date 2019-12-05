from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyHashSet:
    def MD5(self,key):
        h = MD5.new()
        h.update(key.encode("utf-8")) 
        h = int(h.hexdigest(),16)
        return h
  
    def __init__(self, capacity=5):
        ##capacity的bucket
        self.capacity = capacity
        self.data = [None] * capacity
    
    def add(self, key):
        
        number = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        index = number % self.capacity
        
        if self.data[index] == None:
            self.data[index] = ListNode(number)
            
        else:
            new_node = ListNode(number)
            new_node.next = self.data[index]
            self.data[index] = new_node
            
      def remove(self, key):

        while self.contains(key) != False:
            number = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
            index = number % self.capacity
            blank = self.data[index]
            
            if blank.val == number:
                self.data[index] = blank.next
                self.remove(key)
                return
            
            pointer = None
            while blank: 
                if blank.val == number and blank.next:
                    pointer.next = blank.next
                    break
                
                elif blank.val == number and blank.next is None:
                    pointer.next = None
                    break
                    
                elif blank.val != number:
                    pointer = blank
                    blank = blank.next
                    
            self.remove(key)
            
##參考資料
##https://www.nosuchfield.com/2016/07/29/the-python-implementationp-of-HashTable/
##http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html
##https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/
