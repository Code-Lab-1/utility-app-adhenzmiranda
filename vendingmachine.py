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
    'qty' : 1,
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
    'qty' : 2,
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
    'qty' : 1,
     },
     
              { 
    'itemname' : 'Mango Juice',
    'itemno' : 10,
    'price' : 3,
    'qty' : 1,
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
    'qty' : 1,
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
    'qty' : 1,
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
    'qty' : 1,
     },
]


def drinks():
  print("==============DRINKS=============")
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
  print("==============SNACKS==============")
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
  for item, price in snacks_items.items():
    print(f" {item:30}, {price}")


#printing the menu
def menu():
  drinks()
  snacks()

def order():



  while True:
    menu()
    credits = int(input('Please insert an amount to proceed to buy\n'))
    #invalid amount
    if credits == 0:
      print('Please enter a valid amount\n')
      order()

    iteminput = int(input('Please input the number of your desired item\n'))
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
            print(f"You picked {di['itemname']}")
            di['qty'] = di.get('qty', 0) - 1

            total_sum.append(di.get('price'))
            cart.append(di.get('itemname'))
            print(f"Amount of {di['itemname']} remaining: {di['qty']}")
            print("You may now proceed a receive the following items that have been dispensed:\n")
            print(cart,'\n')
            total=sum(total_sum)
            print("And here is your total amount:", total, "AED\n")
            change = credits - total
            print("And your change is:", change, "AED\n")
            print("Thank you for your patronage")
            break

def vendingmachine():
  order()

vendingmachine()