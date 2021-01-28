treeHeight = int(input("enter number of star in tree : "))
i = 0
edspace = ""
star = ""
while i < treeHeight:
    star += " *"
    j = treeHeight
    while j > i:
        edspace = edspace + " "
        j -= 1
    print(edspace + star)
    edspace = ""
    i += 1
if treeHeight > 6:
    i = 0
    while i < treeHeight/4:
        j = treeHeight-1
        while j > 0:
            edspace = edspace + " "
            j -= 1
        print(edspace+"|   |")
        edspace = ""
        i += 1
    j = treeHeight-1
    while j > 0:
        edspace = edspace + " "
        j -= 1
    print(edspace+" ———")
elif treeHeight > 1:
    j = treeHeight
    while j > 0:
        edspace = edspace + " "
        j -= 1
    print(edspace+" |")
else:
    print("Zero Is Invalid")
