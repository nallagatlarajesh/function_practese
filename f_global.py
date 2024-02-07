#example for global value 
#firat i will crfeate a variable 
n=10
def func4():
    print(n)
#i will difine another function
def func5():
    print(n)
    func4()
#main
func5()
