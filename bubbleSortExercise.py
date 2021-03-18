#Modify bubble_sort function such that it can sort following list of transactions happening in an electronic store,

#elements = [
 #       { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
 #       { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
 #       { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
 #       { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
 #   ]
#bubble_sort function should take key from a transaction record and sort the list as per that key. For example,

#bubble_sort(elements, key='transaction_amount')
#This will sort elements by transaction_amount and your sorted list will look like,

#elements = [
#        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#       { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#    ]
#But if you call it like this,

#bubble_sort(elements, key='name')
#output will be,

#elements = [
 #       { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
  #      { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
   #     { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
    #    { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    #]

def bubbleSort(elements, key = None):
	
	for count in range(len(elements)-1):
		swapped = False
		for swi in range(len(elements)-1-count):
			if elements[swi][key] > elements[swi+1][key]:
				elements[swi][key], elements[swi+1][key] = elements[swi+1][key], elements[swi][key]
				swapped = True
		
		if not swapped:
			break
		
	return elements
	
	
if __name__ == "__main__":
	elements = [
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    ]
	
	print("elements: ", elements)
	result = bubbleSort(elements, key = 'transaction_amount')
	print("Sorted List: ")
	for swi in elements:
		print(swi)