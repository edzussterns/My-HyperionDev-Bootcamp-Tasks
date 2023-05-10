# Empty lists to store names and birthdates
names = []
birth_dates = []

# Open the file and read each line (with utf-8 encoding)
with open("DOB.txt", "r", encoding="utf-8") as f:
    for line in f:
        # Split the line into first name, last name, date, month, and year
        first_name, last_name, date, month, year = line.split()
        # Append the first and last name to the 'names' list
        names.append(f"{first_name} {last_name}")
        # Append the date, month and year to the 'birth_dates' list
        birth_dates.append(f"{date} {month} {year}")

# Join each list with a newline separator and print the the names and birthdates
print("Name")
print("\n".join(names))
print("\nBithdate")
print("\n".join(birth_dates))