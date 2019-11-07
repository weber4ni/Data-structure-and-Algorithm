 #### merge_sort_06170138.py
class Solution():
    def mergeList(self,left, right):# self功用連結mege_sort、left、right
         if len(left) == 0:#如果左邊沒有值
             return right#回傳右邊
         if len(right) == 0:
             return left
         if left[0] <= right[0]:#合併完後left、right的第一個值比大小，較小的放入左邊數列，且回傳到left
             return [left[0]]+self.mergeList(left[1:], right)
         if left[0] >= right[0]: #與上段相反，且還回傳到right[]
             return [right[0]]+self.mergeList(left, right[1:])

    def merge_sort(self,nums):
         if len(nums)<=1:#如果list只有一個值，直接回傳
             return nums
         mid = len(nums)//2#找出中間值
         left = nums[:mid]# left值=0~mid
         right = nums[mid:]#right值=mid~-1

         leftData = self.merge_sort(left)#把leftdata裡的值藉由merge_sort、mergeList連結起來
         rightData = self.merge_sort(right)#同上

         return self.mergeList(leftData, rightData)#回傳2值
#參考資料:https://github.com/jeff880714/lesson/blob/master/HW2/heap_sort_06170118.py
