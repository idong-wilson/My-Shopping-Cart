# Takes in an input
# Stores user input into a dictionary or list
# The User can add or delete items
# The User can see current shopping list
# The program Loops until user 'quits'
# Upon quiting the program, prints out a receipt of the items with total and quantity.

my_cart = []

def shoppingDecision(addItem, input1):
  while True:
    shoppingCart = input("What would you like to do? add / remove / show / checkout / quit ")
    if shoppingCart.lower() == "add":
      addItem = input('add what? ')
      quantity = input('quantity ')
      price = input('price ')
      my_cart.append(addItem) 
      
    elif shoppingCart.lower() == "show":
      print(my_cart)
   
    elif shoppingCart.lower() == "remove":
      input1 = input(f'remove what: {my_cart} ')
      if input1 in my_cart:
        my_cart.remove(input1)
        print(f'{input1} removed...')

    elif input1 in my_cart:
      my_cart.remove(input1)
      
    elif shoppingCart.lower() == "checkout":
      for addItem in my_cart:
        print(f"Thanks for purchasing {my_cart}: '\n'see you next time!")
        break

    elif shoppingCart.lower() == "quit":
      print("Thank you! We hope you find what you're looking for next time")
      break

    else:
      print("Please try a valid command.")

shoppingDecision(addItem='', input1='')