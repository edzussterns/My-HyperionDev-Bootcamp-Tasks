# Error message for invalid input
error_Message = "Invalid input. Try again."

# Promt user to enter the number of students registering
while True:
  try:
    num_students = int(input("Enter number of students registering: "))
    break
  except ValueError:
    print(error_Message)

# Loop through each student and get their ID number
for i in range(num_students):
  while True:
    try:
      Student_ID = int(input(f"ID number (student #{i + 1}): "))
      # Open file in "append" mode to avoid overwriting previous entries
      with open("reg_form.txt", "a") as f:
        # Write student ID followed by a dotted line
        f.write(f"{Student_ID} \t{'.'*30}\n")
      break
    except ValueError:
      # Print an error message if the user enters invalid input
      print(error_Message)