#local and global variables 
#local variable
def func1():
    n=5
    print("n val;id is ",n)
    
def func2():
    n=10
    print("n value is ",n)
    func1()
#main
func2()
