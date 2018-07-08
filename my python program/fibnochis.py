def fib(n=10):
        lst=[]
        first = 1
        second = 2
        x = 2
        if(n<2):
            lst = [-1]
            return lst
        else:
            lst = [first, second]
            while(x<n):
                third = first + second
                lst.append(third)
                first = second
                second = third
                x = x+1
            return lst


fib(10)
