## Heapsort
---------------------
Heap的原意是「堆」的意思，Heapsort的特點就是完全以二元樹的方式呈現。子節點的值always 小於 或 大於 父節點，且每個節點又可分左子堆、右子堆。
1.把一個list轉成二元樹後，2每個父節點都要比子節點大，從二元樹下面的數字開始比較。3.再把最大的樹依序提出來。重復1、2動作直到只剩一個數值。





## 學習歷程
<img src="https://github.com/weberliao/Data-structure-and-Algorithm/blob/README.md/85390.jpg" height='700' weight='550'>
一.知道heap堆積的方式、原理之後，就開始用以前會用的程式碼，先拼湊起來，試者想想那些會用到

1.data[]    每次最大值提出來要裝的空間       
2.a = len(nums)  變數nums的個數    
3.pop           提出最大值
4.append        將最大值放置數列最後

二.接下來就是我認為比較困難的部分，寫迴圈。我是先找出重複的動作，並比較何時數字會有要交換的時候

1.left = 2*k+1 , right = 2*k+2  k++

三.我發現根本不用管ｋ的部分，只要與選到的節點，看是要跟left or right比，在2*k+1，2*k+2就好了




## Heapsort流程圖
<img src="https://github.com/weberliao/Data-structure-and-Algorithm/blob/README.md/546.png"　height='700' weight='550'>
