#a dictionary inside a list that's hidden and makes the order() function function to the corrsponding item
drinks_menu = [
    { 
    'itemname' : 'Pepsi',
    'itemno' : 1,
    'price' : 3,
    'qty' : 4,
     },

         { 
    'itemname' : 'Coca-Cola',
    'itemno' : 2,
    'price' : 3,
    'qty' : 2,
     },

         { 
    'itemname' : 'Fanta',
    'itemno' : 3,
    'price' : 3,
    'qty' : 1,
     },
     
              { 
    'itemname' : 'Sprite',
    'itemno' : 4,
    'price' : 3,
    'qty' : 3,
     },
     
              { 
    'itemname' : '7UP',
    'itemno' : 5,
    'price' : 3,
    'qty' : 1,
     },
     
         { 
    'itemname' : 'Sparkling Water',
    'itemno' : 6,
    'price' : 5,
    'qty' : 4,
     },

         { 
    'itemname' : 'Water',
    'itemno' : 7,
    'price' : 1,
    'qty' : 7,
     },

         { 
    'itemname' : 'Chocolate Milk',
    'itemno' : 8,
    'price' : 3,
    'qty' : 1,
     },
     
              { 
    'itemname' : 'Strawberry Milk',
    'itemno' : 9,
    'price' : 3,
    'qty' : 12,
     },
     
              { 
    'itemname' : 'Mango Juice',
    'itemno' : 10,
    'price' : 3,
    'qty' : 9,
     },
         { 
    'itemname' : 'OatVille Biscuits',
    'itemno' : 11,
    'price' : 3,
    'qty' : 4,
     },

         { 
    'itemname' : 'Frito Lays Chips Salt',
    'itemno' : 12,
    'price' : 3,
    'qty' : 2,
     },

         { 
    'itemname' : 'Frito Lays Chips Cheese',
    'itemno' : 13,
    'price' : 3,
    'qty' : 14,
     },
     
              { 
    'itemname' : 'Frito Lays Chips Spicy',
    'itemno' : 14,
    'price' : 3,
    'qty' : 1,
     },
     
              { 
    'itemname' : 'FunYuns',
    'itemno' : 15,
    'price' : 5,
    'qty' : 6,
     },

         { 
    'itemname' : 'KitKat',
    'itemno' : 16,
    'price' : 2,
    'qty' : 4,
     },

         { 
    'itemname' : 'Oreo',
    'itemno' : 17,
    'price' : 2,
    'qty' : 2,
     },

         { 
    'itemname' : 'Lotus Biscuit',
    'itemno' : 18,
    'price' : 2,
    'qty' : 1,
     },
     
              { 
    'itemname' : 'Fudgee Barr Chocolate',
    'itemno' : 19,
    'price' : 3,
    'qty' : 1,
     },
     
              { 
    'itemname' : 'Fudgee Barr Macapuno',
    'itemno' : 20,
    'price' : 6,
    'qty' : 8,
     },
]

#printing drinks and logo
def drinks():
  print("==========VMart-Vending-Machine========")
  print("=================DRINKS================")
  drinks = {
    "01 Pepsi" : "3 AED", 
    "02 Coca-Cola" : "3 AED",
    "03 Fanta" : "3 AED",
    "04 Sprite" : "3 AED",
    "05 7UP" : "3 AED",
    "06 Sparkling Water" : "5 AED",
    "07 Water" : "1 AED",
    "08 Chocolate Milk" : "2 AED",
    "09 Strawberry Milk" : "2 AED",
    "10 Mango Juice" : "2 AED",
}
  for item, price in drinks.items():
    print(f" {item:30}, {price}")

#printing snacks
def snacks():
  print("=================SNACKS================")
  snacks_items = {
    "11 OatVille Biscuit" : "3 AED", 
    "12 Frito Lays Salt" : "3 AED",
    "13 Frito Lays Cheese" : "3 AED",
    "14 Frito Lays Spicy" : "3 AED",
    "15 FunYuns" : "3 AED",
    "16 KitKat" : "5 AED",
    "17 Oreo" : "1 AED",
    "18 Lotus Biscuit" : "2 AED",
    "19 Fudgee Bar Chocolate" : "2 AED",
    "20 Fudgee Bar Macapuno" : "2 AED",
}
#a for loop system that prints out the dictionary like a menu
  for item, price in snacks_items.items():
    print(f" {item:30}, {price}")
  print()


#printing the menu function
def menu():
  drinks()
  snacks()

#the main ordering system
def order():

  #a while loop that starts the function
  while True:
    
    #prints the menu
    menu()

    #asks user input of the credits
    credits = int(input('Please insert an amount to proceed to buy an item in the vending machine:\n'))

    #invalid amount
    if credits == 0:
      print('Please enter a valid amount\n')
      order()

    #asks user input of the displayed items
    iteminput = int(input('Please input the number of your desired item\n'))
    
    #product does not exist message
    if iteminput >= 21:
      print('Product does not exist or is invalid')
      
    cart = []
    total_sum = []

    for di in drinks_menu:

          #insufficient funds
          if iteminput == di['itemno'] and credits <= di['price'] :
            print('Insufficient funds, please kindly re-enter the appropriate amount\n')
            order()

          #out of stock
          if iteminput == di['itemno'] and di['qty'] <= 0:
            print(f"{di['itemname']} is currently out of stock please choose another item \n")
            order()

          #inputting the item 
          if iteminput == di['itemno'] and credits >= di['price']:

            #displays the item the user picked
            print('=======================================\n')
            print(f"You picked {di['itemname']}\n")
            print('=======================================\n')

            #reduces the stock quantity by 1
            di['qty'] = di.get('qty', 0) - 1

            #appends the price into the list of total_sum
            total_sum.append(di.get('price'))
            
            #appends the item into the cart
            cart.append(di.get('itemname'))

            #prints the remaining stock of the item
            print(f"Amount of {di['itemname']} remaining: {di['qty']}\n")

            #prints the the item being dispensed
            print('=======================================\n')
            print("You may now proceed a receive the following items that have been dispensed:\n")

            #prints the cart
            print(cart, '\n')
            print('=======================================\n')

            #prints the total
            total=sum(total_sum)
            print("And here is your total amount:\n\n\t", total, "AED\n")

            #prints the change
            change = credits - total
            print("And your change is:\n\n\t", change, "AED\n")

            #prints the final message
            print('=======================================\n')
            print("Thank you for your patronage!\n")
            print('=======================================\n')

            #breaks the for loop function and starts over again
            break

#renaming the function to vending machine
def vendingmachine():
  order()

#output:
vendingmachine()