
"""
Vending Machine
"""

        
def prices(product, price): # function to calculate the money
    money=float(input("Enter the amount: "))#user input amount of money
    print("----------------")
    print("")
    if money == price:# if condition 
            print(f"Payment accepted.Your Change:$0 Enjoy your {product}")
    elif money > price:
            y= money - price
            print(f"Payment accepted. Your Change: ${y} \nEnjoy your {product}!")
    elif money < price:
        while money < price:
           x= price - money
           print(f"${x} more")
           print("----------------")
           remaining= float(input(f"Enter the remaining amount ${x}: "))
           money += remaining
           
    else:
        print("Payment not accepted")

    
    # y= money - price
    # print(f"Payment accepted. Your Change: ${y} \nEnjoy your {product}!")
           
            

    
    
def main(): # Function to display and user input
    print("------------VENDING MACHINE------------")
    print("")
    print("------------ITEMS------------")
    items = {
            12: ('Apple Juice', 4.00),
            23: ('Orange Juice',4.00),
            34: ('Mango Juice',4.00),
            45: ('Lays salt', 1.19),
            56: ('Lays Spicy',1.19),
            67: ('Lays Cheese',1.19),
            78: ('Snickers', 4.00),
            89: ('Twix', 2.75),
            99: ('KitKat', 2.00),
            10: ('M&M', 4.25),
            24: ('Water', 1.00),
            14: ('Coca Cola', 3.25),
            17: ('Pepsi', 3.25)
                }
    for key, (product,price) in items.items():
            print(f"{key}: {product} = ${price}")
    
    print("----------------")
    
    ui=int(input("Enter the Item number: "))
    
    product, price = items[ui]#searches the user input in the list
    show= ui in items#declares the user input 
    if show==True:
        print("----------------")
        print(product,'-','$',price)
        prices(product,price)
    else:
        print("Invalid Input")
    
main()

while True:
    print("----------------")
    conti=int(input("Press 1 to get another item or press 2 to finish: "))
    if conti==1 :
        main()
   
    if conti==2:
        print("Thank you for using the vending machine")
        break

    
    

