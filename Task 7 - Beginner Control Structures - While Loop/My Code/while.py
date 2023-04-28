total = 0
count = 0
user_input = input("Enter a number (-1 to exit): ")

# Promt user to input numbers until user wants to stop by entering '-1'
while user_input != "-1":
  try:
    number = float(user_input)  # Try convert user input to float
    total += number # If user input is float add input to total
    count += 1 # Increase count by 1 for every user's input that is float
  # If user's input is not valid print message and promt to enter number again
  except ValueError:
    print("Invalid input - not a number.")
  user_input = input("Enter a number (-1 to exit): ")

# Calculate average and print results
# Round total, count and average to 2 decimal places
average = total / count
print(f"\nTotal: {total:,.2f}")
print(f"Count: {count:,.2f}")
print(f"Average: {average:,.2f}")
