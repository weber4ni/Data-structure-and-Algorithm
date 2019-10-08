# Stack & Queue
____________________________________
# What is Stack & Queue
![image](https://github.com/weberliao/Data-structure-and-Algorithm/blob/README.md/455.jpg)
![image](https://github.com/weberliao/Data-structure-and-Algorithm/blob/README.md/789.png)

# Why we need Stack??
* 編譯器(word、sublime)的 undo 。
* 網頁瀏覽器中回到上一頁功能。
* 任何遞迴(recursion)形式的演算法都可以用 Stack 改寫，例如 Depth-First Search(DFS,深度優先搜尋)

# Stack function
* Push(Data): 把資料放到最上面(最新)。
* Pop: 把資料從最上面(最新)移除。
* Top: 回傳最上面(最新)的資料。
* IsEmpty: 確認stack 裡面是否有資料。
* getSize: 回傳stack 裡的資料個數。

# Why we need Queue??
*應用在其他演算法: 
    Bread-First Search | 廣度優先搜尋
    Tree 的 Level-Order Traversal | 二元樹走訪
* 作業係統被多個程式共享資源時(例如CPU、應表機、網站伺服器)，一次只能執行一個需求，所以需要用 Queue 來安排執行順序。
