for r in range(1,6):
	for c in range(1,r+1):
		if(c%2!=0):
			print("*",end=' ')
		else:
			print("|",end=' ')
	print(" ")