def mergeSort(arr):
	#print("calling mergeSort")
	if len(arr) <= 1:
		return arr

	mid = len(arr)//2

	left = arr[:mid]
	right = arr[mid:]

	left = mergeSort(left)
	right = mergeSort(right)

	return mergeSortTwoArrays(left, right)

def mergeSortTwoArrays(arr1, arr2):
	sortedArray = []
	
	swi = swj = 0
	
	while swi < len(arr1) and swj < len(arr2):
		if arr1[swi] < arr2[swj]:
			sortedArray.append(arr1[swi])
			swi += 1
		else:
			sortedArray.append(arr2[swj])
			swj += 1
	
	if swi < len(arr1):
		for tempswi in range(swi, len(arr1)):
			sortedArray.append(arr1[tempswi])
	if swj < len(arr2):
		for tempswj in range(swj, len(arr2)):
			sortedArray.append(arr2[tempswj])
	
	#while swi < len(arr1):
	#	sortedArray.append(arr1[swi])
	#	swi += 1
		
	#while swj < len(arr2):
	#	sortedArray.append(arr2[swj])
	#	swj += 1
	
	#print("sortedArray: ", sortedArray)
	return sortedArray
	
	
if __name__ == "__main__":
	#arr1 = [5,8,12,56]
	#arr2 = [7,9,45,51]
	
	unsortedArray = [10, 3, 15, 7, 8, 23, 98, 29]
	
	#result = mergeSortTwoArrays(arr1, arr2)
	print(mergeSort(unsortedArray))
	#print("Sorted Array: ", result)