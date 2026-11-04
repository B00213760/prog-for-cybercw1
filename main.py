# Task 5 - Cyber Security Utilities
# Step 1 - Import the functions from security_tools.py

from security_tools import check_password_strength, validate_ip, generate_password

# Step 2 - Ask the user to enter a password
password = input("Enter a password to check its strength: ")

# Step 3 - Check whether the password is strong
if check_password_strength(password):
	print("Strong password")
else:
	print("Weak password")

#Step 4 - Suggest a strong password if the entered password is weak
if not check_password_strength(password):
	print("Suggested strong password:", generate_password())

# Step 5 - Ask the user to enter an IP address
ip_address = input("Enter an IP address to validate: ")

# Step 6 - Check whether the IP address is valid
if validate_ip(ip_address):
	print("Valid IP address")
else:
	print("Invalid IP address")