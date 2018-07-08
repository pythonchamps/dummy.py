for r in range(5,0,-1):
	for c in range(0,r):
		if(r%2!=0):
			print("*",end=' ')
		else:
			print("-",end=' ')
	print(" ")