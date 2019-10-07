# Linked list
_____________________________________

# What is linkd list??
linkd list　是由一連串的node所構成，每個node指向下一個node，最後一個node指向Null( python is None)

# Why we need linked list??
* 這用 linked list 的優點說明比較清楚
    1.新增/刪除資料較簡單:只要對前一個 note 調整 pointer 即可，不須像Array搬動其餘元素。
    2.當我們需要頻繁新增/刪除資料
    3.不需要快速查詢資料
#  main code

*node : 節點
```python=
node1 = ListNode(15)
```  
*listnode*first: 表示第一個node
```python=
class ListNode:
  def __init__(self, data): 
    # store data
    self.data = data
    # store the reference (next item)
    self.next = None
    return
 ```  
*pointer :記錄下一個node的位子，才能在node中移動(travesal)

**補充** 屬性(attribute):每個node本身有2個屬性，一個是本身的值，另一個是pointer

# What is different between ARRAY ??

一張圖看懂ARRAY VS Linked list

