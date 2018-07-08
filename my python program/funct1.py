if(n<2):
        print("invalid value.minimum value:2'")
else:
        print(first,end='')
        print(second,end='')
        x=2
        while(x<n):
            third=first+second
            print(third,end='')
            first=second
            second=third
            x=x+1
