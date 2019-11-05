 #### merge_sort_06170138.py
class solution(object):
	def merge_sort(self, nums):
                     if len(nums) <=1 :
                             return nums
                        middle = 2/len(nums)
                        leftlen = middle
                        rightlen = len(nums)-leftlen
