'''
I have been struggling to find the right way to fit in while loop in function I had for calculating bond as it icluded all inputs related to function.
I asked for help with loops in 'The Coding Den' discord server: https://discord.gg/code. User Kenny pointed out that my functions has very low cohesion and they are responsible for way too much. Suggested to try to split things up more. In terms of good code, the calculate_bond function should do just what it says - calculate the bond, not take any inputs. It would be better to make the calculate_bond take the inputs as parameters.
Kenny also helped to undersand and see where code is dublicating and repeating.
'''
import math

 # Money in outputs is printed with 2 decimal places ('.2f' - this is responsible for this) and large numbers like 100000 are displayed like 100,000 (',' before '.2f' is responsible for this).

# Function to get an input from user.
# I tweaked this function many times with help of few google searches.
# Loop to keep asking user for input until it's the right type or, if nothing has been entered or value is 0.
def get_input(display: str, to_type: type, on_error: str, validate_func=None):
  while True:
    try:
      value = input(display)
      if value.endswith(('k', 'K')): # Accept 'k' or 'K' to for thousand input and convert
        value = float(value[:-1]) * 1000
      elif value.endswith(('m', 'M')):  # Accept 'm' or 'M' for million input and convert
        value = float(value[:-1]) * 1000000
      else:
        value = to_type(value)
      if validate_func and not validate_func(value):
        print(on_error)
        continue
      return value
    except ValueError:
      print(on_error)

# Function to calculate investment with 'simple' or 'compound' interest based on user's choice
def calculate_investment(deposit, interest_rate, years, interest):
  if interest.lower() == "simple":
    total_amount = deposit * (1 + interest_rate / 100 * years)
  elif interest.lower() == "compound":
    total_amount = deposit * math.pow(1 + interest_rate / 100, years)
    
  profit = total_amount - deposit
  # Print results for investment projection including user's inputs for clarification
  print(f"\nIf you invest £ {deposit:,.2f} for {years} years with {interest} interest rate {interest_rate}%, you will get back £ {total_amount:,.2f}. That is £ {profit:,.2f} profit on top of your initial investment!")

# Function to calculate bond if user chooses 'bond' upon first choice
# Print results with formatting - money is displayed with 2 decimal places
def calculate_bond(interest_rate: float, house_value: float, months: int):
  repayment = (interest_rate / 100 / 12 * house_value) / (1 - (1 + interest_rate / 100 / 12)**(-months))
  repayment_total = repayment * months
  # Print results for investment projection including user's inputs for clarification
  print(f'''\nWith present house value of £ {house_value:,.2f}, interest rate of {interest_rate}% and {months} months to repay the bond, you will have to repay £ {repayment:,.2f} each month. That is a total repayment of £ {repayment_total:,.2f}!''')

# Print welcome message and menu shown in collumns
print("* * * Finance Calculator! * * * \n")
print("\033[4mNote\033[0m: '10k', '10M' for numbers are also are accepted.")
print(f"\n{'investment': <10} - to calculate the amount of interest you'll earn on your investment")
print(f"{'bond': <10} - to calculate the amount you'll have to pay on a home loan")

# Error message for output if wrong input
error_msg = "\n***Invalid input.***"

# Promt user to choose 'investment' or 'bond', loop while correct input given
while True:
  user_choice = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ")
  if user_choice.lower() not in ["investment", "bond"]:
    print(error_msg)
    continue
    
  # If 'investment' chosen, promt user for relevant inputs 
  if user_choice.lower() == "investment":
    deposit = get_input("Enter the amount of money you want to deposit (£): ", float, error_msg, lambda x: x > 0)
    interest_rate = get_input("Enter the interest rate (%): ", float, error_msg, lambda x: x > 0)
    years = get_input("Enter the number of years you plan on investing: ", int, error_msg, lambda x: x > 0)
    interest = get_input("Which type of interest you want to invest with? Enter either 'simple' or 'compound': ", str, error_msg, lambda x: len(x) > 0)
    if interest.lower() not in ["simple", "compound"]:
      interest = get_input("Which type of interest you want to invest with? Enter either 'simple' or 'compound': ", str, error_msg, lambda x: len(x) > 0)
      continue

    else:
      calculate_investment(deposit, interest_rate, years, interest)
      # Stop program after results printed
      break

  # If 'bond' chosen, promt user for relevant inputs 
  elif user_choice.lower() == "bond":
    house_value = get_input("Enter present value of the house (e.g. 100000): ", float, error_msg, lambda x: x > 0)
    interest_rate = get_input("Enter the interest rate (%): ", float, error_msg, lambda x: x > 0)
    months = get_input("Enter the number of months you plan to take to repay the bond: ", int, error_msg, lambda x: x > 0)
    calculate_bond(interest_rate, house_value, months)
    # Stop program after results printed
    break