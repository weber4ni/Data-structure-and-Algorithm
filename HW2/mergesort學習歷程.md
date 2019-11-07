## mergesort
-----------------------------------
拆解:先把數列拆解成只剩下一個數字                                                                   
合併:再兩兩互相合併成新數列後。  屬於Divide and Conquer的演算法來執行


## 學習歷程
與heapsort一樣，都是先自己畫完流程圖後，就會比較知道一開始該定義的函數、需要的程式碼是那些。最後找出需要用迴圈、if else跑出的地方。
首先
1.def merge_sort(self, nums):
                     if len(nums) <=1 :
                             return nums
                        middle = 2/len(nums)
                        leftlen = middle
                        rightlen = len(nums)-leftlen
                        這是一開始看流程圖需要的地方
2.                        
<img src="https://github.com/weberliao/Data-structure-and-Algorithm/blob/README.md/merge.jpg" height='700' weight='550'>






## 流程圖
<img src="https://github.com/weberliao/Data-structure-and-Algorithm/blob/README.md/mergesort.png" height='500' weight='350'>
