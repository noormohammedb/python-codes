list = ["first1","second2","third3","forth4","fifth5","sixth6","seventh7"]
print(list[3:-3])
if "second2" in list :
    print("exist")
list.append("eight8")
print(list)
list.remove("first1")
print("removed first1")
print(list)
list.pop()
print("list pop()")
print(list)
del list[3]
print("del list[3]")
print(list)

# copy list
newList = list.copy()
print("newList ")
print(newList)

# List cleared

list.clear()
print("list cleared")
print(list)