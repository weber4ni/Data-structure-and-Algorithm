def quicksort(list):
    left = [ ]
    right = [ ]
    middle = [ ]
    
    if len(list)>1:
        #if條件式只當len裡的數值只剩1個時，停止分類且return
        pivot = list[0] #設第一個數為基準點避免 index out of range

        for i in list:
            if i < pivot:
                left.append(i)
            elif i == pivot:
                middle.append(i)
            else:
                right.append(i)
    else:
        return list

    return quicksort(left) + middle + quicksort(right)
