x=2
    if(n<2):
        lst=[-1]
    else:
        lst=[first,second]
        while(x<n):
            third=first+second
            lst.append(third)
            first=second
            second=third
            x=x=1
            return lst
        fib(1)
        print()