import sys

def main():
	if len(sys.argv) != 4:
		print("fail")
		sys.exit(1)
	
	alphabet = sys.argv[1]
	match_score = sys.argv[2]
	mismatch_score = sys.argv[3]
	
	print("  ", end=" ")
	for c in alphabet: 
		print(c, end="  ")
	print()

	for r in alphabet: 
		print(r, end=" ")
		for c in alphabet:
			if r == c:
				print(match_score, end=" ")
			else: 
				print(mismatch_score, end=" ")
		print()

if __name__ == "__main__": 
	main()