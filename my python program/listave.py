lst=[]
x=int(input("enter no of elements"))
for n in range(x):
	lst.append(int(input("enter no")))
for i in range(x):
	sum=sum+lst[i]
print("average=",sum/x)