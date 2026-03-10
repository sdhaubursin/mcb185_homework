import sys

def main():
	if len(sys.argv) != 2: 
		print("fail")
		sys.exit(1)

n = int(sys.argv[1])

for a in range(1, n + 1):
	for b in range(a, n + 1):
		for c in range(b, n + 1):
			if a*a + b*b == c*c: 
				print(a, b, c)
				
if __name__ == "__main__":
	main()