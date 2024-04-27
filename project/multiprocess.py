import time
import multiprocessing
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
	sys.stdout = open(f"multiprocess-procedure.txt", "w")
	start_time = time.time()

	# process count
	process_count = 3

	# the processes list
	processes = []
	for _ in range(0, process_count):
		process1 = multiprocessing.Process(target=add_number,args=(19999999,))
		process2 = multiprocessing.Process(target=add_number,args=(199999999,))
		process3 = multiprocessing.Process(target=arithmetic,args=(10000,))
		# process4 = multiprocessing.Process(target=io())
		processes.append(process1)
		processes.append(process2)
		processes.append(process3)
		# processes.append(process4)

	#start of processes
	for pro in processes:
		pro.start()

	#check if they are done
	for proc in processes:
		proc.join()

	print(processes)

	print ("Multiprocess done!")
	end_time = time.time()
	print(f'Completed in {end_time-start_time}')
	sys.stdout.close()