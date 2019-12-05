## Hash Table原理
----------------------------
Hash Table希望能夠將存放資料的「Table」的大小(size)降到「真正會存放進Table的資料的數量」，也就是「有用到的Key的數量」

●若有用到的Key之數量為n，Table的大小為m，那麼目標就是m=Θ(n)

※※但是如果碰撞到相同值時，可以使用Linked list把「Hashing到同一個slot」的資料串起來


##流程圖
-----------------------------
<img src="https://github.com/weberliao/Data-structure-and-Algorithm/blob/README.md/5.png" height='700' weight='550'>



參考資料
http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html


