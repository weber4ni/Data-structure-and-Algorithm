## 速度之比較
-------------------------
平均而言，heapsort、mergesort 速度相同


<img src="https://github.com/weberliao/Data-structure-and-Algorithm/blob/README.md/TIME.png" height='200' weight='150'><img src="https://github.com/weberliao/Data-structure-and-Algorithm/blob/README.md/123.png" height='200' weight='150'>


## 程式碼之比較
-------------------------
用到迴圈的地方:

mergesort```if left[0] <= right[0]:

             return [left[0]]+self.mergeList(left[1:], right)
             
             if left[0] >= right[0]: 
         
             return [right[0]]+self.mergeList(left, right[1:])
heapsort
             ```for i in range(n,-1,-1):
             
            if 2*i+1<n and nums[i]<nums[2*i+1]:
            
                nums[i],nums[ 2*i+1]=nums[ 2*i+1],nums[i]
                
            if 2*i+2<n and nums[i]<nums[2*i+2]:
            
                nums[i],nums[2*i+2]=nums[2*i+2],nums[i]#
                
            else:```

## 相同之處
---------------------------


