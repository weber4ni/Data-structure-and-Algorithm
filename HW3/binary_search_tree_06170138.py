class TreeNode(object):
	def _init_(self,x):
		self.val =x
		self.left = None
		self.right = None
		class Solution(object):
			def insert(self ,root,val):
				node1 = TreeNode(val)
				if root.val:
					if x<root.val:
						if root.left is None :
							root.left = TreeNode(x)
					else:
						root.left.insert(x)
				elif x>=root.val:
					if root.rigjt is None :
						root.right = TreeNode(x)
					else:
						root.right.insert(x)
				else:
					root.val = x
