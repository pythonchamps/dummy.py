lst=[1,2]
def function1():
    global lst
    lst=[3,4]
    print(lst)
def function2():
    global lst
    lst=[5,6]
    print(lst)
    function1()
    function2()
    