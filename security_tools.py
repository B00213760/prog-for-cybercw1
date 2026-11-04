# Task 5 - Cyber Security Utilities
# Step 1 - Import modules for generating random passwords

import random
import string

# Step 2 - Create a function to check password strength
def check_password_strength(password):

	# Step 3 - Check that the password is at least 10 characters long
	if len(password) < 10:
		return False

    # Step 4 - Check for uppercase and lowercase letters
	if not any(char.isupper() for char in password):
		return False

	if not any(char.islower() for char in password):
		return False

    # Step 5 - Check for numbers and special characters
	if not any(char.isdigit() for char in password):
		return False

	if not any(char in string.punctuation for char in password):
		return False
	
    # Step 6 - Return True if the password meets all requirements
	return True

# Step 7 - Create a function to validate an IP address
def validate_ip(ip_address):
	ip_address = ip_address.strip()

	# Step 8 - Check that the IP address contains exactly three dots
	if ip_address.count(".") != 3:
		return False

    	# Step 9 - Split the IP address into four sections
	octets = ip_address.split(".")

	if len(octets) != 4:
		return False

    	# Step 10 - Check that each section contains only numbers
	for octet in octets:
		if not octet.isdigit():
			return False

        # Step 11 - Check that each number is between 0 and 255
		number = int(octet)

		if number < 0 or number > 255:
			return False
	# Step 12 - Return True if the IP address is valid
	return True

# Step 13 - Create a function to generate a random password
def generate_password():
	length = random.randint(10, 16)

	# Step 14 - Create a collection of characters for the password
	
	characters = string.ascii_letters + string.digits + string.punctuation

	# Step 15 - Generate a random password using the available characters
	# Step 17 - Keep generating passwords until a strong one is created
	while True:
		password = "".join(random.choice(characters) for i in range(length))

		if check_password_strength(password):
			break
		
	# Step 16 - Return the generated password
	return password
