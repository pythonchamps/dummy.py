perc=float(input("enter percentage"))
grade="  "
if(perc>90):
	grade="A+"

elif(perc>80 and perc<=90):
	grade="A"

elif(perc>70 and perc<=80):
	grade="B+"

elif(perc>60 and perc<=70):
	grade="B"

elif(perc>50 and perc<=60):
	grade="C+"

elif(perc>40 and perc<=50):
	grade="C"

if(perc<40):
	grade="F"
print("grade=",grade)
