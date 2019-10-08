# Linked list
_____________________________________

# What is linked list??
linkd list　是由一連串的node所構成，每個node指向下一個node，最後一個node指向Null( python is None)
![image](https://github.com/weberliao/Data-structure-and-Algorithm/blob/README.md/linked.png)

# Why we need linked list??
* 這用 linked list 的優點說明比較清楚
    1.新增/刪除資料較簡單:只要對前一個 note 調整 pointer 即可，不須像Array搬動其餘元素。
    2.當我們需要頻繁新增/刪除資料
    3.不需要快速查詢資料
#  main code

*node : 節點
```python=
node1 = ListNode(37) //新增一個37數字到著個節點裡
```  
*len(list):要計算元素個數的列表

*listnode: 如何建置
```python=
class ListNode:
  def __init__(self, data): 
    
    self.data = data                  //store data
    self.next = None                  //store the reference (next item)
    return
 ```  
*pointer :記錄下一個node的位子，才能在node中移動(travesal)

*Single Linked-list:在建立list的一開始，我們預設裡面是沒有節點的。而linked-list本身帶有head跟tail兩個屬性
接下來試著建立一個 自己的 list 
```python=
class SingleLinkedList:
  def __init__(self):                 //initialize this object
    self.head = None
    self.tail = None
    reture     
    
def add_list_item(self, item):        // make sure item is a proper node  
   if not isinstance(item, ListNode):
    item = ListNode(item) 
   if self.head is None:
    self.head = item
  else:
    self.tail.next = item
    self.tail = item
  return     
    
list1 = SingleLinkedList()
list1.add_list_item(node1)
list1.add_list_item(38)              // 建置好list1 內有37、38兩個數值
 ```
 

**補充**: 屬性(attribute):每個node本身有2個屬性，一個是本身的值，另一個是pointer

# What is different between ARRAY ??

一張圖看懂ARRAY VS Linked list
![image](https://github.com/weberliao/Data-structure-and-Algorithm/blob/README.md/differ.png)
