def quicksort(list):
    left = [ ]
    right = [ ]
    middle = [ ]
    
    if len(list)>=1:     #if條件指當len裡的數值只剩1個時，停止分類且return
        pivot = list[0]    #設第一個數為基準點，避免若剩下1個數字時 index out of range

        for i in list:
            if i < pivot:     #qiucksort概念，把數值小的放置左邊
                left.append(i)
            elif i == pivot:   #若抓到的數字與基準點相同，先抓出來
                middle.append(i)
            else:                # 其餘的值放置右邊
                right.append(i)
    else:
        return list

    return quicksort(left) + middle + quicksort(right)
