def bubbleSort(elements):
	
	for count in range(len(elements)-1):
		swapped = False
		print("Current List: ", elements)
		#subtracting count as the last elements will be sorted anyway so no point in go through them
		for swi in range(len(elements)-1 - count):
			if elements[swi] > elements[swi+1]:
				elements[swi], elements[swi+1] = elements[swi+1], elements[swi]
				swapped = True
		
		#Breaking the loop as array is already sorted		
		if swapped == False:
			break
	
	
	return elements
	
if __name__ == "__main__":
	elements = [5, 9, 2, 1, 67, 34, 88, 34]
	result = bubbleSort(elements)
	print("Sorted Array: ", result)
	
	
	elements = [1,2,3,4,5,6,7,8,9]
	result = bubbleSort(elements)
	print("Sorted Array: ", result)