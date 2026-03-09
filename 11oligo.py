def calculate_oligi_tm(a, c, g, t): 
	n = a + c + g + t
	gc_count = (g + c)
	at_count = (a + t)
	
	if n <= 13: 
		tm = (at_count * 2) + (gc_count * 2)
	else: 
		tm = 64.9 + 41 * (gc_count - 16.4) / n
	return round(tm, 2)
print(calculate_oligi_tm(3, 4, 5, 7))
print(calculate_oligi_tm(2, 1, 3, 4))