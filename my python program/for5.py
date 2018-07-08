for r in range(1,6):
	for c in range(1,6):
		if(r==2 or r==3 or r==4):
			if(c==2 or c==3 or c==4):
				print(" ",end=' ')
			else:
				print("*",end=' ')
		else:
			print("*",end=' ')

	print(" ")