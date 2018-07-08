def listreverse(lst):
    n=len(lst)
    for x in range(0,n//2):
        lst[x],lst[n-1-x]=lst[n-1-x],lst[x]
        return lst
    print(list.reverse[10,20,30,40])