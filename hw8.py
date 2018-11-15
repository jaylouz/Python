
import random

#This function take in starting and ending value to print random numbers onto a filename
def random_number_file_create(min, max, filename, entries): 
	for x in range(entries):
		numb = random.randrange(min,max)
		file = open(filename, "a")
		file.write(str(numb) + "\n")
		#file = open(filename, 'r')
		#print(file.read())
	file.close()

def lines_print(filename):
	print("-----------------------")
	total = 0
	count = 0
	file = open(filename, 'r')
	for x in file:
		print(x)
		total += int(x)
		count += 1
	#print("Average: " + str(total/count))
	file.close()
		
def lines_count(filename):
	with open(filename) as f:
		for i, l in enumerate(f):
			pass
	return i + 1
	print(i)

def total_numbers_in_file(filename):
	totalNumebrs = 0
	file = open(filename, 'r')
	for x in file:
		file.readlines()
		totalNumebrs += int(x)
	print(totalNumebrs)



FILENAME = "numbers.txt"
random.seed(83)
random_number_file_create(1, 10, FILENAME, 10)
lines_print(FILENAME)
print()
entries = lines_count(FILENAME)
print("Entries:", entries)
total   = total_numbers_in_file(FILENAME)
average = round(total/entries)
print("Total:", total)
print("Average:", average)


