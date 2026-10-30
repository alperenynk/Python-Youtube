# Variable Scope = where a variable is visible and accessible
# Scope Resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

def func1():
    a = 1
    print(a)

def func2():
    a = 2
    print(a)

func1()
func2()
