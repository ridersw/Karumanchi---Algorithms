def insertionSort(elements):
	
	for swi in range(1, len(elements)):
		anchor = elements[swi]
		swj = swi - 1
		
		while swj >= 0 and elements[swj] > anchor:
			elements[swj+1] = elements[swj]
			swj -= 1
	
		elements[swj+1] = anchor
	
if __name__ == "__main__":
	elements = [11, 9, 29, 7, 2, 15, 28]
	insertionSort(elements)
	print(elements)