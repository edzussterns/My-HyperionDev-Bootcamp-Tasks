# Prompt user to input a string and handle error if user didn't entered anything
while True:
    string = input("Enter a string: ")

    if string.strip() == "":
        print("\nYou didn't enter anything.\n")
        continue
    else:
        break

formatted_string = ""

# If character's index is even, format character to upper
# If character's index is odd, format character to lower
for char_index in range(len(string)):
    if char_index % 2 == 0:
        formatted_string += string[char_index].upper()
    else:
        formatted_string += string[char_index].lower()

print(formatted_string)

# Split user's string into words
words = string.split()
formatted_words = []

# If the index is even, format the word to all lower case
# If the index is odd, format the word to all upper case
for word_index in range(len(words)):
    if word_index % 2 == 0:
        formatted_words.append(words[word_index].lower())
    else:
        formatted_words.append(words[word_index].upper())

# Join words back together and print result
print(' '.join(formatted_words))
