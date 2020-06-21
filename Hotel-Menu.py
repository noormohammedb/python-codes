print("Select From list ")
menu = ["1 . Mutta Biriyani","2 . Chicken Biriyani","3 . Neychoorum Beefum","4 . Mutton Biriyani","5 . Kultha Kanji"]
for x in menu :
    print(x)
option = int(input())
if option == 1 :
    print("You'r Selection Is Mutta Biriyani")
elif option == 2 :
    print("You'r Selection Is Chicken Biriyani")
elif option == 3 :
    print("You'r Selection Is Neychoorum Beefum")
elif option == 4 :
    print("You'r Selection Is Mutton Biriyani")
elif option == 5 :
    print("You'r Selection Is Kultha Kanji")
else :
    print("Invalid")