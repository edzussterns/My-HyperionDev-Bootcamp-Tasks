# Function calculates the total worth of all stock
# Loops through the menu list and multiplies the quantity of each item in stock by its price
# Returns the total stock value
def calculate_total_stock_value(menu, stock, price):
    total_stock_value = 0
    item_values = {}
    for item in menu:
        quantity = stock.get(item, 0)
        item_price = price.get(item, 0)
        item_value = quantity * item_price
        total_stock_value += item_value
        item_values[item] = {'quantity': quantity, 'price': item_price, 'value': item_value}
    return total_stock_value, item_values

menu = ['Espresso', 'Tea', 'Hot Chocolate', 'Special Cookie', 'Jimba Jamba', 'Gugu Gaga']
stock = {
  menu[0]: 450, # Espresso
  menu[1]: 500, # Tea
  menu[2]: 250, # Hot Chocolate
  menu[3]: 80,  # Special Cookie
  menu[4]: 50,  # Jimba Jamba
  menu[5]: 75 # Gugu Gaga
  }
price = {
  menu[0]: 2.50,  # Espresso
  menu[1]: 2.00, # Tea
  menu[2]: 3.00, # Hot Chocolate
  menu[3]: 11.50,  # Special Cookie
  menu[4]: 8.50,  # Jimba Jamba
  menu[5]: 3.50 # Gugu Gaga
  }

# Print out the worth, quantity, and price of each item in stock and total worth of all stock
# Display results in table sort of look
# '.ljust()' is a string method that pads the string with spaces to the left.
# Reference: https://www.tutorialspoint.com/python/string_ljust.htm
total_stock_value, item_values = calculate_total_stock_value(menu, stock, price)
print("="*47)
print("\tCafe Stock Inventory")
print("="*47)
print(f"\n{'Item'.ljust(15)}| {'Quantity'.ljust(9)}| {'Price'.ljust(8)}| Worth")
print("-"*47)
for item, values in item_values.items():
    print(f"{item.ljust(15)}| {str(values['quantity']).ljust(9)}| ${str(values['price']).ljust(7)}| ${values['value']:8.2f}")
print("-"*47)
print(f"{'Total'.ljust(36)}| ${total_stock_value:8.2f}")