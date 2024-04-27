import time
import threading
import sys


def add_number(number2: int):
	"""
	A CPU-heavy operation! Checking
	if the number is bigger than the other one.
	"""
	start = time.time()
	number1 = 0
	while number1 < number2:
		number1 = number1 + 1
	end = time.time()
	print(f'Finished counting to {number2} in {end-start}')
	return number1

def arithmetic(number3: int):
	"""
	Completes math operations.
	"""
	start = time.time()
	number1 = 100
	number2 = 100
	while number1 > number3:
		number1 = number1 + 100
	print(number3)
	end = time.time()
	print(f'Finished math with {number1} {number2} {number3} in {end-start}')
	return number3

def io():
	"""
	IO Heavy task
	"""
	start = time.time()
	for _ in range(3):
		print("One")
		time.sleep(1)
		print("Two")
		time.sleep(1)
		print("Three")
	end = time.time()
	print(f'Finished counting to Three, 3 times, in {end-start}')


if __name__ == "__main__":
	sys.stdout = open(f"multithread-procedure.txt", "w")
	start_time = time.time()

	# thread count
	thread_count = 3

	# the threads list
	threads = []
	for _ in range(0,thread_count):
		# thread1 = threading.Thread(target=add_number,args=(19999999,))
		# thread2 = threading.Thread(target=add_number,args=(199999999,))
		# thread3 = threading.Thread(target=arithmetic,args=(10000,))
		thread4 = threading.Thread(target=io())
		# threads.append(thread1)
		# threads.append(thread2)
		# threads.append(thread3)
		threads.append(thread4)

	#start threads
	for thr in threads:
		thr.start()

	#check if they are done
	for thrs in threads:
		thrs.join()

	print(threads)

	print ("Multithreading done!")
	end_time = time.time()
	print(f'Completed in {end_time-start_time}')
	sys.stdout.close()