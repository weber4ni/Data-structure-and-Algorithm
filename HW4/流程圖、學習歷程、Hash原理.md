## Hash Table原理
----------------------------
資料放到雜湊表時，先給定一個 key 和存放的 value，並將 key 的每個字元轉換成 ASCII Code 或 Unicode Code 並相加，這個相加的值即是 hash 鍵值，在 table 陣列上對應到存放的 value

## Hash Function的功用
----------------------------
Hash Function 是將輸入的數字、文字轉譯成特定的職，特性為單向性、不可逆性，Hash Function好不好用是Hash Table 的關鍵

※※但是如果碰撞到相同值時，可以使用Linked list把「Hashing到同一個slot」的資料串起來


## 流程圖
-----------------------------
<img src="https://github.com/weberliao/Data-structure-and-Algorithm/blob/README.md/5.png" height='700' weight='550'>

## 學習歷程 
-----------------------------
參考資料

http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html
https://blog.kdchang.cc/2016/09/23/javascript-data-structure-algorithm-dictionary-hash-table/
https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/


