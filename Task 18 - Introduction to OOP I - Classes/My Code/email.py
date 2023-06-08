### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email:
    def __init__(self, email_address, subject_line, email_content):
        # Initialise the instance variables for emails.
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        # Declare the class variable, with default value, for emails.
        self.has_been_read = False

    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True

# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    """
    A function which creates an email object with the email address, subject line and contents, and stores it in the Inbox list.
    
    At program start-up, this function is used to populate the Inbox with three sample email objects for further use in this program.
    """
    # Create 3 sample emails.
    email_1 = Email("one@mail.com", "Welcome to HyperionDev!", "Congratulations, you have now enrolled in HyperionDev bootcamp!")
    email_2 = Email("two@mail.com", "Great work on the bootcamp!", "You are doing great on your Skills Bootcamp - Software Engineering!")
    email_3 = Email("three@mail.com", "Your excellent marks!", "We would like to congratulate you on your outsatnding marks!")
    
    # Add sample emails to the Inbox list.
    inbox.extend([email_1, email_2, email_3])

def list_emails():
    """
    A function that loops through the Inbox and prints the email’s subject_line, along with a corresponding number.
    
    For example, if there are three emails in the Inbox:
        0 Welcome to HyperionDev!
        1 Great work on the bootcamp!
        2 Your excellent marks!
    """
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    for index, email in enumerate(inbox):
        print(f"{index}.\t{email.subject_line}")
        print("--------------------------------------------------")

# Create a function which displays a selected email.
def read_email(index):
    """
    A function that displays a selected email, together with the email_address, subject_line, and email_contents, and then sets its has_been_read instance variable to True.
    """ 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    if 0 <= index < len(inbox):
        email = inbox[index]
        print("\n--------------------------------------------------")
        print("From:    ",email.email_address)
        print("Subject: ", email.subject_line)
        print("Content: ", email.email_content)
        print("--------------------------------------------------")
        email.mark_as_read()
        print(f"\nEmail from '{email.email_address}' marked as read.")
        input("\nPress ENTER to continue...")
    else:
        print("Invalid email index.")

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
populate_inbox()

print("Welcome to Email Simulator!")

# Fill in the logic for the various menu operations.
while True:
    user_choice = input('''\nWould you like to:
1. Read an email
2. View unread emails
3. Quit application

Enter selection: ''')
       
    if user_choice == '1':
        # add logic here to read an email
        if len(inbox) > 0:
            # Display the list of emails to choose from
            print("\nInbox:")
            print("--------------------------------------------------")
            list_emails()

            try:
                email_index = int(input("Enter the number of the email to read: "))
                read_email(email_index)
            except ValueError:
                print("\nInvalid input for email number. Try again.")
            except IndexError:
                print("\nInvalid input for email number. Try again.")
        else:
            print("\nInbox is empty.")

    elif user_choice == '2':
        # add logic here to view unread emails
        unread_emails = [email for email in inbox if not email.has_been_read]
        if unread_emails:
            print("\nUnread Emails:")
            print("--------------------------------------------------")
            for index, email in enumerate(unread_emails):
                print(f"{index}.\t{email.subject_line}")
                print("--------------------------------------------------")
            try:
                email_index = int(input("Enter the number of the email to read: "))
                read_email(email_index)
            except ValueError:
                print("\nInvalid input for email number. Try again.")
            except IndexError:
                print("\nInvalid input for email number. Try again.")
        else:
            print("\nThere are no unread emails.")
            
    elif user_choice == '3':
        # add logic here to quit appplication
        print("Good Bye!")
        break
        
    else:
        print("\nOops - incorrect input.")