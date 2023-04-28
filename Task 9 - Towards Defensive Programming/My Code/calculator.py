# Function to get an input from user. Used same function in task 5.
def get_input(display: str, to_type: type, on_error: str, validate_func=None):
  while True:
    try:
      value = input(display)
      value = to_type(value)
      if validate_func and not validate_func(value):
        print(on_error)
        continue
      return value
    except ValueError:
      print(on_error)

# Functions for +, -, *, /
def add(num1, num2):
  return num1 + num2
def subtract(num1, num2):
  return num1 - num2
def multiply(num1, num2):
  return num1 * num2
def divide(num1, num2):
  if num2 == 0:
    print("\nInvalid operation. In math it is not allowed to divide by zero.")
  else:
    return num1 / num2

# Dictionary of operators for functions
operator_functions = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

error_msg = "Invalid input. Try again."

# Promt user to choose either to enter enter numbers and operation or read equations from file
user_choice = get_input("Enter '1' to enter numbers and operation or '2' to read equations from a txt file: \n", int, "Invalid choice. Try again.", lambda x: x in [1, 2])

# If user choice 1 - promt user to enter numbers and operation
if user_choice == 1:
  num1 = get_input("Enter 1st number:  ", float, error_msg)
  num2 = get_input("Enter 2nd number:  ", float, error_msg)
  operator = get_input("Enter operator (+,-,*,/): ", str, error_msg)
  while True:
    # Check if operator is valid
    if operator not in operator_functions:
        print("Invalid operator. Try again.")
        operator = get_input("Enter operator (+,-,*,/): ", str, error_msg)
    else:
        result = operator_functions[operator](num1, num2)
        print(f"\nResult: {num1} {operator} {num2} = {result}")
        # Write equation to text file
        with open("equations.txt", "a") as file:
          file.write(f"{num1} {operator} {num2} = {result}\n")
          break
# Else if 2 - promt user to enter name of text file to read equations from
else:
  while True:
    try:
      file_name = input("Enter the name of the file to read (include file extension .txt): ")
      file_name = open(file_name, "r")
      # Read over the lines in text file
      read_lines = file_name.read()
      print(read_lines)
      file_name.close()
      break
    # Handle error if user entered wrong file name or file not found
    except FileNotFoundError as error:
      print(f"'{file_name}' does not exist. Try gain.")