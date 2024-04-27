import multiprocessing
import multithread
from subprocess import call

def open_multithread():
	call(["python", "multithread.py"])

def open_multiprocess():
	call(["python", "multiprocess.py"])

print("Welcome to the Multithreading and Multiprocessing Simulator!\n")

def menu():
	print("\t[1] Multithreading")
	print("\t[2] Multiprocessing")
	print("\t[0] Exit the program")


menu()
option = int(input("\nEnter your option: "))

while option != 0:
	if option == 1:
		print("\n\tMultithreading!")
		print("\t.......")
		open_multithread()
		print("\n\tMultithreading done!")
	elif option == 2:
		print("\n\tMultiprocessing!")
		print("\t.......")
		open_multiprocess()
		print("\n\tMultiprocessing done!")
	elif option == 0:
		pass
	else:
		print("Invalid option!")

	print()
	menu()
	option = int(input("\nEnter your option: "))