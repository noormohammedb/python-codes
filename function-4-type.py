# Function with no argument and no return value

"""print("enter 2 number")
def main():
    fnumber = int(input("1. : "))
    snumber = int(input("2. : "))
    print("sum = ",fnumber+snumber)
main()"""



# Function with no argument and a return value

"""print("enter 2 number")
def main():
    fnumber = int(input("1. : "))
    snumber = int(input("2. : "))
    return fnumber+snumber
print("sum = ",main())"""




# Function with  argument and no return value


"""print("enter 2 number ")

def main(arg1,arg2):
    print("sum = ",arg1+arg2)

num1 = int(input("1. : "))
num2 = int(input("2. : "))
main(num1,num2)"""




# Function with argument and a return value


print("enter 2 number ")

def main(arg1,arg2):
    return arg1+arg2

num1 = int(input("1. : "))
num2 = int(input("2. : "))
print("sum = ",main(num1,num2))