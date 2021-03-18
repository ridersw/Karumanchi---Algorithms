class binaryTree:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		
	def addChild(self, data):
		#print("Data: ", data)
		if data == self.data:
			return
			
		if data < self.data:
			if self.left:
				self.left.addChild(data)
			else:
				self.left = binaryTree(data)
		else:
			if self.right:
				self.right.addChild(data)
			else:
				self.right = binaryTree(data)
		
	def inorderTraversal(self):
		elements = []
		
		if self.left:
			elements += self.left.inorderTraversal()
			
		elements.append(self.data)
		
		if self.right:
			elements += self.right.inorderTraversal()
			
		return elements

def buildTree(numbers):
	root = binaryTree(numbers[0])
	
	for swi in range(1, len(numbers)):
		root.addChild(numbers[swi])
		
	return root


if __name__ == "__main__":
	numbers = [17, 4, 1, 20, 9, 23, 18, 34]
	
	binaryTree = buildTree(numbers)
	
	print("Root: ", binaryTree.data)
	print("Inorder Traversal: ", binaryTree.inorderTraversal())
	
	