 class Solution():
    def heapify(self,nums):
        n=len(nums)#n等於nums裡的個數
        for i in range(n,-1,-1):#在nums範圍裡的最後一個開始往前
            if 2*i+1<n and nums[i]<nums[2*i+1]:#設L= 2*j+1，若l存在、選到的nums[i]節點的左邊支線做比較
                nums[i],nums[ 2*i+1]=nums[ 2*i+1],nums[i]#若符合上述條件，2數交換
            if 2*i+2<n and nums[i]<nums[2*i+2]:#設R= 2*j+2，若r存在、選到的nums[i]節點的右邊支線做比較
                nums[i],nums[2*i+2]=nums[2*i+2],nums[i]#若符合上述條件，2數交換
            else:
                continue
    def heap_sort(self,nums):
        data=[]#每次heapify好時，把值放在這裡
        n=len(nums)#n等於nums裡的個數
        for j in range(n):#nums裡幾個數字就跑幾次
            self.heapify(nums)
            data.append(nums.pop(0))#插入data[]，從nums的最大值
            data[: :-1]#因為是maxhea所以反轉過來
        return data#返回data
