from passmanager import store_passwords, verify_master_password
from passmanagerfunctions import password, send_email
import secrets

secret = secrets.token_hex(16)
passw = input("Please provide the master password: ")
verify = verify_master_password()
recipient_email = input("Please provide the email address to send the token:\n")
send = send_email(secret, recipient_email)
token = input("Please provide the token in the email")


if verify == True and token == secret:
    print("Login Success!")
else:
    print("Login Failed")
    exit()

txt = input("Please provide an easy password for this site:\n")
app_name = input("Please provide the name of the site:\n").lower()
password = password(txt, app_name, 12)
email = input("Please provide the email:\n")
user = input("Please provide the username if applicable:\n")
if user == None:
    user = ''
url = input('Please paste the url:\n')
store_passwords(password, email, user, url, app_name)
print('Password stored in database!')
