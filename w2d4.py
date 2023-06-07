# Questioon 1
#Module should have the following capabilities:

#1a) Has a function to calculate the square footage of a house
#Reminder of Formula: Length X Width == Area
#1b) Has a function to calculate the circumference of a circle 2 Pi r

import math

def calculate_square_footage(length, width):
    return length * width

def calculate_circumference(radius):
    return 2 * math.pi * radius

length = float(input("Enter the length of the house: "))
width = float(input("Enter the width of the house: "))

square_footage = math.calculate_square_footage(length, width)
print("The square footage of the house is:", square_footage)

radius = float(input("Enter the radius of the circle: "))

circumference = math.calculate_circumference(radius)
print("The circumference of the circle is:", circumference)

# Question 2
#Build a Shopping Cart Function
#You can use either lists or dictionaries. The program should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list

def shopping_cart():
    cart = []  
    
    while True:
        print("1. Add item")
        print("2. Remove item")
        print("3. Show shopping list")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            item = input("Enter the item to add: ")
            cart.append(item)
            print("Item added to the shopping cart.")
        
        elif choice == "2":
            item = input("Enter the item to remove: ")
            if item in cart:
                cart.remove(item)
                print("Item removed from the shopping cart.")
            else:
                print("Item not found in the shopping cart.")
        
        elif choice == "3":
            print("Current shopping list:")
            for item in cart:
                print(item)
        
        elif choice == "4":
            print("Items in your shopping list:")
            for item in cart:
                print(item)
            break
        
        else:
            print("Invalid choice. Please enter a valid option (1-4).")

shopping_cart()