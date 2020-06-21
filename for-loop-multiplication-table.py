fnum = int(input("Multiplication Table \nEnter Number And Limit : "))
limit = int(input("Limit : "))
table = 0
print("\nTable : \n")
for i in range(fnum,fnum*limit+1,fnum) :
    table = table + 1
    print(str(table) + " X " + str(fnum) + " = " + str(i))