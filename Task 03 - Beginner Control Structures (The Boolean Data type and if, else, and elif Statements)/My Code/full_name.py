# Promt user to input their full name until it is entered correctly.
while True:
  full_name = input("Enter your full name: \n")
  
  # Split input to check if user entered 2 names
  full_name_list = full_name.split()
  
  # Store the lenght of full name
  full_name_lenght = len(full_name)

  # Check if anything has been entered at all
  if full_name_lenght == 0:
      print("You haven't entered anything. Please enter your full name.")
      continue
  # Check if at least 2 words have been entered
  elif len(full_name_list) == 1:
      print("You entered less than 2 words. Please make sure that you have entered your name and surname.")
      continue
  else:
    # Check if entered name is too short
    if full_name_lenght < 4:
      print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
      continue
    # Check if entered name is too long
    elif full_name_lenght > 25:
      print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
      continue
    # Exit the loop if the name is entered correctly
    else:
      print("Thank you for entering your name.")
      break
