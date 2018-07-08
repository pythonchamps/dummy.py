sal=float(input("enter your salary"))
ts=0
if(sal<=10000):
	ts=1.2*sal

elif(sal<=20000):
	ts=1.1*sal

else:
	ts=1.05*sal

print("your total salary=",ts)