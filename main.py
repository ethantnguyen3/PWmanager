from passmanager import store_passwords, verify_master_password
from passmanagerfunctions import password, send_email
from menu import menu, create, find, find_accounts
import secrets

# Generate a random token for two-factor authentication
secret = secrets.token_hex(16)

# Prompt for master password to verify access
passw = input("Please provide the master password: ")
verify = verify_master_password()  # Call function to verify the master password

# Collect the recipient's email for sending the authentication token
recipient_email = input("Please provide the email address to send the token:\n")

# Send the generated token to the provided email
send_email(secret, recipient_email)

# Prompt user to input the token sent to their email
token = input("Please provide the token in the email")

# Verify both the master password and the token
if verify == True and token == secret:
    print("Login Success!")
else:
    print("Login Failed")
    exit()

while choice.upper() != 'Q':
    choice = menu()
    if choice == '1':
        create()
    elif choice == '2':
        find_accounts()
    elif choice == '3':
        find()
    else:
        print("Invalid option. Please select a valid menu option.") 
        continue 

print("Exiting the program. Goodbye!")



