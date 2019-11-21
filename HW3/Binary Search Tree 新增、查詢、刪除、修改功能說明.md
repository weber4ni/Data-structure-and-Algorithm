## Binary Search Tree(二元搜尋樹)
-------------------------------
特殊關鍵
● 搜尋、排序都需要「比大小」
● 每個node最多2個子節點，可能沒有
● 若是>=放right, <放left，TREE頂點右邊所有值都會大於左邊所有的值

## 新增
-------------------------
根據 >=放right, <放left的規則跟最開始的node做比較， 如果是null直接新增值進去

## 查詢(A值)
---------------------------
● 若一開始就search到A--->ture
●再根據>=放right, <放left，若A>node往右找，反之往左找

參考資料:http://alrightchiu.github.io/SecondRound/binary-search-tree-introjian-jie.html
