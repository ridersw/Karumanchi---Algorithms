def selectionSort(arr):
	
	size = len(elements)
	
	for swi in range(len(elements)-1):
		minIndex = swi
		for swj in range(minIndex+1, size):
			if elements[swj] < elements[minIndex]:
				minIndex = swj
		
		if swi != minIndex:
			elements[swi], elements[minIndex] = elements[minIndex], elements[swi]
	
if __name__ == "__main__":
	elements = [78, 12, 15, 8, 61, 53, 23, 27]
	selectionSort(elements)
	print("Sorted Array: ", elements)