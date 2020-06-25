def function_main():
    def function_sub1():
        variable = "sub 1"
        print("Executed function_sub1 , variable = ",variable)
    def function_sub2():
        nonlocal variable
        variable = "sub 2"
        print("Executed function_sub2 , nonlocal variable = ",variable)
    def function_sub3():
        global variable
        variable = "sub 3"
        print("Executed function_sub3 , global variable = ",variable)

    def display():
        print("Executed display in function_main ,  variable = ",variable)

    variable = "default"
    print("\nvariable declared in function_main() before calling any with value of ",variable)

    function_sub1()
    print("after execution of function_sub1 , variable = ",variable)
    
    function_sub2()
    print("after execution of function_sub2 , variable = ",variable)

    function_sub3()
    print("after execution of function_sub3 , variable = ",variable)

    display()
    print("\nvariable declared in function_main() after calling all with value of ",variable)


variable = "global"
print("\nProgram Starting\nBefore calling function_main() variable = ",variable)

function_main()

print("\nAfter calling function_main() variable = ",variable)