## introduce Quicksort
-------------------------
## 基本概念
使用Divide and Conquer的演算法來實作。概念是從數列中挑選一個基準點(pivot)，大於基準的放一邊，小於的放一邊，直到該下一個為未排序，循環最後即可完成排序。

*Divide and Conquer :先劃分，再解決。優點:1.困難的問題簡化為容易實作的方式
                                         2.能夠平行處理
        
*in-plcae :在蒐集資料時，找到許多相關資料，便來看看差異。基本概念:將基準點暫時移到最右邊，小於基準的移至數列一端並記錄遞增索引，最後將基準點換回索 
                                                              引位置。
                                                        
## 流程圖
<img src="https://github.com/weberliao/Data-structure-and-Algorithm/blob/README.md/asd.jpg" height='500' weight='350'>

## 不適合使用的時機
因為適用迴圈的方式來運作，所以當不是合用迴圈時，也不適合使用，會減少效率 。EX :費波那西數列(fibonacci)

