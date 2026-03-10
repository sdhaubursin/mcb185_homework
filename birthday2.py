import sys
import random

def main():
	if len(sys.argv) != 3:
		print("fail")
		sys.exit(1)
		
	c = int(sys.argv[1]) # calendar size
	n = int(sys.argv[2]) # number of people
	calendar = [0] * c

	for i in range(n):
		birthday = random.randint(0, c - 1)
		calendar[birthday] += 1
	
	if calendar[birthday] > 1: 
		print("match found")
	else: 
		print("no match")
			
if __name__ == "__main__":
	main()