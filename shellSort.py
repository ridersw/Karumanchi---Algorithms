import time

def shellSort(arr):
	
	count = 0
	
	size = len(arr)
	gap = size // 2
		
	while gap > 0:
		for swi in range(gap, size):
			anchor = arr[swi]
			swj = swi
			
			while swj >= gap and arr[swj - gap] > anchor:
				arr[swj] = arr[swj - gap]
				count += 1
				swj -= gap
				
			arr[swj] = anchor
			#print("Array: ", arr)
			count += 1
			
		gap = gap // 2
	
	#print("No of Swaps: ", count)
	return
	
def insertionSort1(n, arr):
	
	count = 0
	
	for swi in range(1, len(arr)):
		anchor = arr[swi]
		swj = swi - 1
		
		while swj >= 0 and arr[swj] > anchor:
			arr[swj+1] = arr[swj]
			count += 1
			swj -= 1
			
		arr[swj + 1] = anchor
		count += 1
		#print("Array: ", arr)
		
	#print("No of Swaps: ", count)

if __name__ == "__main__":
	arr = [8,0,1,5,7,1,98]
	t1 = time.time()
	shellSort(arr)
	e1 = time.time()
	print("Time Required for ShellSort: ", e1 - t1)
	
	
	