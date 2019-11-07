## 速度之比較
-------------------------
平均而言，heapsort、mergesort 速度相同


<img src="https://github.com/weberliao/Data-structure-and-Algorithm/blob/README.md/TIME.png" height='200' weight='150'><img src="https://github.com/weberliao/Data-structure-and-Algorithm/blob/README.md/123.png" height='200' weight='150'>


## 程式碼之比較
-------------------------
用到迴圈的地方:mergesort```if left[0] <= right[0]:#合併完後left、right的第一個值比大小，較小的放入左邊數列，且回傳到left
             return [left[0]]+self.mergeList(left[1:], right)
         if left[0] >= right[0]: #與上段相反，且還回傳到right[]
             return [right[0]]+self.mergeList(left, right[1:])```
             heapsort```for i in range(n,-1,-1):#在nums範圍裡的最後一個開始往前
            if 2*i+1<n and nums[i]<nums[2*i+1]:#設L= 2*j+1，若l存在、選到的nums[i]節點的左邊支線做比較
                nums[i],nums[ 2*i+1]=nums[ 2*i+1],nums[i]#若符合上述條件，2數交換
            if 2*i+2<n and nums[i]<nums[2*i+2]:#設R= 2*j+2，若r存在、選到的nums[i]節點的右邊支線做比較
                nums[i],nums[2*i+2]=nums[2*i+2],nums[i]#若符合上述條件，2數交換
            else:```

## 相同之處
---------------------------


