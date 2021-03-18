#Modify merge_sort function such that it can sort following list of athletes as per the time taken by them in the marathon,

#elements = [
#        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
#        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
#        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
#        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
#    ]
#merge_sort function should take key from an athlete's marathon log and sort the list as per that key. For example,

#merge_sort(elements, key='time_hours', descending=True)
#This will sort elements by time_hours and your sorted list will look like,

#elements = [
#        {'name': 'rajab', 'age': 12, 'time_hours': 3},
#        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
#        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
#        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
#    ]
#But if you call it like this,

#merge_sort(elements, key='name')
#output will be,

#elements = [
#        { 'name': 'chinmay',   'age': 24, 'time_hours': 1.5},
#        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
#        { 'name': 'vedanth',  'age': 17,  'time_hours': 1},
#        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
#    ]


def mergeSort(arr, key, ascending = None):
	if len(arr) <= 1:
		return 
		
	mid = len(arr) // 2
	left = arr[:mid]
	right = arr[mid:]
	
	mergeSort(left, key)
	mergeSort(right, key)
	
	mergeSortTwoArrays(left, right, arr, key)
	
def mergeSortTwoArrays(arr1, arr2, arr, key):
	swi = swj = swk = 0
	
	while swi < len(arr1) and swj < len(arr2):
		if arr1[swi][key] < arr2[swj][key]:
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
	elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
	
	#arr = [5,1,3,9,6,8,0]
	#mergeSort(elements, key = 'time_hours')
	mergeSort(elements, key = 'name')
	print(elements)
	#reversing the elements
	print(elements[::-1])
	
	