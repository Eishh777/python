#we are gonna make a small menu handeling program in python 
#we will use a dictionary to store the menu items

menu = {
    "pizza": 340, 
    "burger" : 250,
    "fries" :150,
    "soda" :100,
    "coffee":140
}
#displaying menu
for items in menu:
    print(f"the price of {items} is {menu[items]}")


order=input("Enter the items u wanna order: ")
total=0

if order in menu:
    total+=menu[order]
else:
    print("sorry thats not available ")    

order2=input("do u wanna order anything else(y/n): ")

if (order2.lower()=="y"):
    n=int(input("how many more do u wanna order: "))

    while(n>0):
        order3=input("enter more items u wanna order: ") 
        if order3 in menu: 

            total+=menu[order3]
            n-=1
        else:
            print("order unavailable.")

else: 
    print("order placed!")
print("total cost is ", total)



        



