'''
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
''' 

from hash_maker import password
import subprocess
from database_manager import store_passwords, find_users, find_password

def menu():
    # Display the main menu and return the user's choice
    print('-' * 30)
    print(' ' * 11 + 'Menu' + ' ' * 11)
    print('1. Create new password')
    print('2. Find all sites and apps connected to an email')
    print('3. Find a password for a site or app')
    print('Q. Exit')
    print('-' * 30)
    return input('Select an option (1, 2, 3, Q): ').strip()

def create():
    # Collect details to create and store a new password entry
    print('Please provide the name of the site or app you want to generate a password for:')
    app_name = input().strip()
    if not app_name:
        print("App/site name cannot be empty.")
        return

    print('Please provide a simple password for this site:')
    plaintext = input().strip()
    if not plaintext:
        print("Password cannot be empty.")
        return

    # Generate a secure password and copy it to clipboard
    passw = password(plaintext, app_name, 12)
    try:
        subprocess.run('xclip', universal_newlines=True, input=passw)
        print("Your password has been created and copied to your clipboard.")
    except FileNotFoundError:
        print("xclip not found; unable to copy password to clipboard.")

    # Gather additional information to store the password entry
    user_email = input('Please provide a user email for this app or site: ').strip()
    username = input('Please provide a username for this app or site (if applicable): ').strip()
    if not username:
        username = ''
    url = input('Please paste the URL to the site that you are creating the password for: ').strip()

    # Store the password in the database
    store_passwords(passw, user_email, username, url, app_name)
    print("Password created and stored successfully!")

def find():
    # Find a password for a specific site or app
    print('Please provide the name of the site or app you want to find the password for:')
    app_name = input().strip()
    if not app_name:
        print("App/site name cannot be empty.")
        return
    find_password(app_name)

def find_accounts():
    # Find all accounts associated with a given email
    print('Please provide the email that you want to find accounts for:')
    user_email = input().strip()
    if not user_email:
        print("Email cannot be empty.")
        return
    find_users(user_email)

def main():
    # Main loop for handling menu actions
    while True:
        choice = menu()
        if choice == '1':
            create()
        elif choice == '2':
            find_accounts()
        elif choice == '3':
            find()
        elif choice.upper() == 'Q':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid menu option.")


