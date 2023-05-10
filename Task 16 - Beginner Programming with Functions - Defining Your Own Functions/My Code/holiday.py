# This program calculates the cost of a holiday based on the destination, duration of stay at hotel, and duration of car rental.

# Funtion for getting input
# Reference: 'get_input' fuction used in Task 5, modified.
def get_input(display: str, to_type: type, on_error: str, validate_func=None):
  while True:
    try:
      value = input(display)
      value = to_type(value)
      if validate_func and not validate_func(value):
        print(on_error) # string to display when input is invalid
        continue
      return value
    except ValueError:
      print(on_error)
# Function to calculate the total cost for hotel stay  
def hotel_cost(city_flight, num_nights):
  # Get the cost per night for the chosen destination
  hotel_cost_per_night = destinations.get(city_flight)[1]
  return num_nights * hotel_cost_per_night

# Function to calculate the cost of plane ticket
def plane_cost(city_flight):
  return destinations.get(city_flight)[0]

# Function to calculate the car rental
def car_rental(num_days, city_flight):
  return num_days * destinations.get(city_flight)[2]

# Function to calculate the total cost of the holiday
def holiday_cost(city_flight, num_nights, num_days):
  # Calculate the total cost for the holiday
  total_cost = hotel_cost(city_flight, num_nights) + plane_cost(city_flight) + car_rental(num_days, city_flight)
  return total_cost

on_error = "\n* Invalid input.\n"

# Define the options for destinations and their costs
destinations = {
  # 'destination': [Plane Cost, Hotel Cost per night, Car Rental Cost per day]
  'Hong Kong, China': [550.99, 100.99, 50.99],
  'Macau, China': [800, 80, 40],
  'Riga, Latvia': [1150, 25, 20],
  'Singapore, Singapore': [479, 50, 50],
  'Sydney, Australia': [1200, 120, 70],
  'Cairo, Egypt': [940, 58, 35],
  'Istanbul, Turkey': [480, 60, 30],
  'Bangkok, Thailand': [1000, 90, 60]}

print("=" * 40)
print("\tHoliday Cost Calculator")
print("=" * 40)

# Print the destination options from 'destinations' dictionary
print("Destination options:")
for i, destination in enumerate(destinations.keys()): # Reference: https://realpython.com/python-enumerate/
  print(f"  {i+1} - {destination}")

# Prompt the user to choose the destination from options
while True:
  try:
    choice = get_input(f"\nPlease enter option 1 to {len(destinations)}: ", int, "\n* Oops, that's invalid option.", lambda x: x > 0)
    # Handle the user input thats greater than the greatest option number
    if choice > len(destinations):
      print("\n* Oops, there are not that many options.")
      continue
    # Assign the new value to 'city_flight' based on the user choice
    city_flight = list(destinations.keys())[choice - 1]
    break
  except (ValueError, IndexError):
    print(on_error)

# Prompt the user to enter duration of stay at hotel
while True:
  try:
    num_nights = get_input("Enter number of nights you will be staying at hotel: ", int, on_error)
    # Handle the user input thats not in range 1 to 365
    if num_nights < 1 or num_nights > 365:
      print("\n* Duration must must be in range 1 to 365. Try again.\n")
      continue
    else:
      break
  except (ValueError):
    print(on_error)

# Prompt the user to enter duration of hiring car
while True:
  try:
    num_days = get_input("Enter number of days you will be hiring car for: ", int, on_error)
    # Handle the user input thats not in range 1 to 365
    if num_days < 1 or num_days > 365:
      print("\n* Duration must must be in range 1 to 365. Try again.\n")
      continue
    else:
      break
  except (ValueError):
    print(on_error)

# Calculate the total holiday cost and print out the details in 2 collumns
total_cost = holiday_cost(city_flight, num_nights, num_days)
print(f'''\nYour holiday details:
  - Destination: \t{city_flight}
  - Plane Cost: \t£ {plane_cost(city_flight):,.2f}
  - Hotel Cost: \t£ {hotel_cost(city_flight, num_nights):,.2f} for {num_nights} nights
  - Car Rental Cost: \t£ {car_rental(num_days, city_flight):,.2f} for {num_days} days
  
  - Total Holiday Cost: £ {total_cost:,.2f}''')
