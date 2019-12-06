from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
def add(self, key):
        h = MD5.new()
        h = int(temp,16)
        index = h % self.capacity
        if self.data[index] == None:
            self.data[index] = ListNode(temp)
            return
        else:
            node = self.data[index]
            while node:
                if node.val == temp:
                    return
                if node.next == None:
                    node.next = ListNode(temp)
                    return
                node = node.next
def remove(self, key):
        key_int = MyHashSet.Hash(self, key)
        index = key_int % self.capacity
        node_head = self.data[index]
        if node_head:
            if node_head.val == key_int :
                node_head=node_head.next
                self.data[index] = node_head
        if node_head : 
            while node_head.next:
                if node_head.next.val == key_int:
                    node_head.next = node_head.next.next
                    
                    
                else:
                    node_head = node_head.next
            
##參考資料
##https://www.nosuchfield.com/2016/07/29/the-python-implementationp-of-HashTable/
##http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html
##https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/
##https://github.com/C-WeiYu/WeiYu/blob/master/HW4/hash_table_06170201.py
