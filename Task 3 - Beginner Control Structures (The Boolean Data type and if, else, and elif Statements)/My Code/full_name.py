# Keep asking the user for their full name until it is entered correctly.
while True: 
  full_name = input("Enter your full name: \n") # Ask the user to input their full name

  full_name_list = full_name.split() # Split input to check if user entered 2 names
  full_name_lenght = len(full_name) # Store the lenght of full name

  if full_name_lenght == 0: # Check if anything has been entered at all
      print("You haven't entered anything. Please enter your full name.")
      continue

  elif len(full_name_list) == 1: # Check if at least 2 words have been entered
      print("You entered less than 2 words. Please make sure that you have entered your name and surname.")
      continue

  else: 
    if full_name_lenght < 4: # Check if entered name is too short
      print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
      continue

    elif full_name_lenght > 25: # Check if entered name is too long
      print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
      continue

    else:
      print("Thank you for entering your name.")
      break # Exit the loop if the name is entered correctly