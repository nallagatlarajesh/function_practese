#variable lenght argument
def func1(*mylist):
    for num in mylist:
        print(num)
    return
#main
func1(10,20,30)
func1(2,3)
func1(1,2,3,4)
