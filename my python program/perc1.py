perc=float(input("enter percentage"))
grade="  "
if(perc<40):
	grade="F"

elif(perc>=40 ):
	grade="C"

elif(perc<50):
	grade="C+"

elif(perc<60 ):
	grade="B"

elif(perc<70 ):
	grade="B+"

elif(perc<80):
	grade="A"

if(perc<90):
	grade="A+"
print("grade=",grade)
