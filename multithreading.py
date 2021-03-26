import time
import threading

def calSquare(arr):
	print("Calculating Square")
	for n in arr:
		time.sleep(0.2)
		print("Square: ", n * n)
		
def calCube(arr):
	print("Calculating Cube")
	for n in arr:
		time.sleep(0.2)
		print("Cube: ", n * n * n)
		
		
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

t = time.time()

t1 = threading.Thread(target = calSquare, args = (arr,))
t2 = threading.Thread(target = calCube, args = (arr,))

t1.start()
t2.start()

t1.join() #wait function for t1
t2.join() #wait function for t2

print("Time Require: ", time.time() - t)

#Without Multithreading: Time Require:  8.010646104812622

#with multithreading: 4.016311407089233
