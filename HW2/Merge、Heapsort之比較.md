## 速度之比較
-------------------------
平均而言，heapsort、mergesort 速度相同


<img src="https://github.com/weberliao/Data-structure-and-Algorithm/blob/README.md/TIME.png" height='200' weight='150'><img src="https://github.com/weberliao/Data-structure-and-Algorithm/blob/README.md/123.png" height='200' weight='150'>


## 程式碼之比較
-------------------------
用到迴圈的地方:

mergesort```
             if left[0] <= right[0]:

             return [left[0]]+self.mergeList(left[1:], right)
             
             if left[0] >= right[0]: 
         
             return [right[0]]+self.mergeList(left, right[1:])
        ```
heapsort
         ```
             for i in range(n,-1,-1):
             
            if 2*i+1<n and nums[i]<nums[2*i+1]:
            
                nums[i],nums[ 2*i+1]=nums[ 2*i+1],nums[i]
                
            if 2*i+2<n and nums[i]<nums[2*i+2]:
            
                nums[i],nums[2*i+2]=nums[2*i+2],nums[i]#
                
            else:
                  continue
            ```

## 相同之處
---------------------------
因為這次有用到self回傳變數的問題，參考查了許多回傳的關鍵方法，技巧在於設變數放的位子要在主要執行程式的地方
for example mergesort
```
 def merge_sort(self,nums):
         if len(nums)<=1:#如果list只有一個值，直接回傳
             return nums
         mid = len(nums)//2#找出中間值
         left = nums[:mid]# left值=0~mid
         right = nums[mid:]#right值=mid~-1
```


