#optimizing Space Complexity

def mergeSort(arr):
	if len(arr) <= 1:
		return
		
	mid = len(arr) // 2	
	left = arr[:mid]
	right = arr[mid:]
	
	mergeSort(left)
	mergeSort(right)
	
	mergeSortTwoArrays(left, right, arr)
	
def mergeSortTwoArrays(arr1, arr2, arr):
	swi = swj = swk = 0
	
	while swi < len(arr1) and swj < len(arr2):
		#print("Checking for swi: ", arr1[swi], " and swj: ", arr2[swj])
		if arr1[swi] < arr2[swj]:
			arr[swk] = arr1[swi]
			swi += 1
		else:
			arr[swk] = arr2[swj]
			swj += 1
		swk += 1
		
	while swi < len(arr1):
		arr[swk] = arr1[swi]
		swi += 1
		swk += 1
		
	while swj < len(arr2):
		arr[swk] = arr2[swj]
		swj += 1
		swk += 1
	
if __name__ == "__main__":
	#arr = [10, 3, 15, 7, 8, 23, 98, 29]
	#arr1 = [3, 7, 10, 15]
	#arr2 = [8, 23, 29, 98]
	#print(mergeSortTwoArrays(arr1, arr2))
	#mergeSort(arr)
	#print(arr)
	
	testCases = [
		[10, 3, 15, 7, 8, 23, 98, 29],
		[],
		[3],
		[9, 8, 7, 2],
		[1, 2, 3, 4, 5]
	]
	
	for testcase in testCases:
		mergeSort(testcase)
		print(testcase)