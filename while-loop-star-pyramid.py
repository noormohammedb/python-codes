i = 0
j = 33
k = 0
l = 6

while i<=l :
    j = 33
    while j>=i :
        print(" ",end='')
        j = j - 1
    k = 0
    while k<=i :
        print("* ",end='')
        k = k + 1
    print("")
    i = i + 1