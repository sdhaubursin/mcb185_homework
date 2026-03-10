import sys
import random

def main():
	if len(sys.argv) != 3:
		print("fail")
		sys.exit(1)
		
	c = int(sys.argv[1]) # calendar size
	n = int(sys.argv[2]) # number of people
	people = []

	for i in range(n):
		birthday = random.randint(1, c)
		people.append(birthday)
	
	for i in range(n):
		for j in range(i + 1, n):
			if people[i] == people[j]:
				print("match found")
			else: 
				print("match not found")
			
if __name__ == "__main__":
	main()