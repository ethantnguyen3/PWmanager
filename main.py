from passmanager import store_passwords, verify_master_password
from passmanagerfunctions import password, send_email
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

# Collect user inputs to create and store a new password entry
txt = input("Please provide an easy password for this site:\n")
app_name = input("Please provide the name of the site:\n").lower()

# Generate a strong password based on the easy password and site name
password = password(txt, app_name, 12)

# Get additional details for the password entry
email = input("Please provide the email:\n")
user = input("Please provide the username if applicable:\n")
if user == None:  # If no username is provided, default to an empty string
    user = ''
url = input('Please paste the url:\n')

# Store the new password and related details in the database
store_passwords(password, email, user, url, app_name)
print('Password stored in database!')
